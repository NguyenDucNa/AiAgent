import json
import Levenshtein
from typing import List

from src.tools.utils.call_api import call_api

def get_location_id(
    url: str,
    session_id: str,
    location_name: str,
    locations: List[dict] = None
) -> str | List[dict] | None:
    if locations is None:
        locations: List[dict] = get_all_locations(url, session_id)
    if locations:
        return map_name_to_id(location_name, locations)

def get_room_id(
    url: str,
    session_id: str,
    room_name: str,
    rooms: List[dict] = None
) -> str | List[dict] | None:
    if rooms is None:
        rooms: List[dict] = get_all_rooms(url, session_id)
    if rooms:
        return map_name_to_id(room_name, rooms)
    
def get_all_locations(
    url: str,
    session_id: str
) -> List[dict]:
    data: List[dict] = get_locations_rooms(url, session_id).get("data", [])
    return [{
        "name": item.get("location_name"),
        "id": item.get("location_id")
    } for item in data]

def get_all_rooms(
    url: str,
    session_id: str
) -> List[dict]:
    data: List[dict] = []
    for item in get_locations_rooms(url, session_id).get("data", []):
        # location_name = item.get("location_name", "")
        # location_id = item.get("location_id", "")
        for room in item.get("rooms", []):
            data.append({
                "id": room.get("room_id", ""),
                "name": room.get("room_name", "")
            })
    return data

def map_name_to_id(
    source_name: str,
    targets: list[dict] = None,
    lower_threshold: float = 0.75,
    ambiguous_threshold: float = 0.1
) -> str | List[dict] | None:
    # targets: [{"name": "", "id": ""}]
    cands: List[tuple] = []
    for item in targets:
        if normalize_name(item["name"]) == normalize_name(source_name):
            return item["id"]

        score: float = compute_similarity(item["name"], source_name)
        if score >= lower_threshold:
            cands.append((score, item))

    cands: List[tuple] = sorted(cands, key=lambda x: x[0], reverse=True)
    if (
        (len(cands) == 1) or
        (len(cands) > 1 and cands[0][0] == 1.0) or
        (len(cands) > 1 and cands[0][0] - cands[1][0] >= ambiguous_threshold)
    ):
        return cands[0][-1]["id"]

def compute_similarity(sa: str, sb: str) -> float:
    sa: str = normalize_name(sa)
    sb: str = normalize_name(sb)
    longer_s, shorter_s = (sa, sb) if len(sa) >= len(sb) else (sb, sa)

    if shorter_s in longer_s:
        return 1.0

    max_score: float = 0.0
    for i in range(len(longer_s) - len(shorter_s) + 1):
        substring: str = longer_s[i:i + len(shorter_s)]
        distance: int = Levenshtein.distance(substring, shorter_s)
        score: float = 1 - (distance / max(len(substring), len(shorter_s)))
        if score >= max_score:
            max_score = score
    return max_score

def normalize_name(name: str) -> str:
    return " ".join(name.split()).lower()

def get_locations_rooms(
    url: str,
    session_id: str,
) -> dict:
    # call api
    data = {
        "type": "function_calling",
        "message": {
            "name": "bookingroom@action#get_locations_rooms",
            "natural_name": "",
            "params": [],
            "category": "report"
        }
    }
    status_code, body, api_log = call_api(url, session_id, data)
    
    # parse outputs
    data: list[dict] = []

    if status_code == 200:
        body: dict = json.loads(body)
        for item in body.get("payload") or []:
            loc_name: str = item.get("LocationName") or ""
            loc_id: str = item.get("LocationID")
            loc_id = str(loc_id) if loc_id is not None else ""

            rooms: list[dict] = []
            for room in item.get("ListRoom") or []:
                room_id: str = room.get("RoomID")
                room_id = str(room_id) if room_id is not None else ""
                rooms.append({
                    "room_name": room.get("RoomName") or "",
                    "room_id": room_id
                })
            data.append({
                "location_name": loc_name,
                "location_id": loc_id,
                "rooms": rooms
            })

    return {
        "data": data
    }