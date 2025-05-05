import json
from typing import Optional, List

from src.tools.utils.call_api import call_api

def get_person_id(
    url: str,
    session_id: str,
    person_name: str,
    employee_code: Optional[str] = "",
    organization_id: Optional[str] = "",
    organization_name: Optional[str] = ""
) -> str | List[dict] | None:
    person_name: str = normalize_string(person_name)
    employee_code: str = normalize_string(employee_code)
    organization_id: str = normalize_string(organization_id)
    organization_name: str = normalize_string(organization_name)

    data: List[dict] = get_personal_information(
        url,
        session_id,
        person_name,
        employee_code,
        organization_id,
        organization_name
    ).get("data", [])

    if len(data) == 1:
        return data[0].get("person_id", "")
    return data

def get_employee_code(
    url: str,
    session_id: str,
    person_name: str,
    employee_code: Optional[str] = "",
    organization_id: Optional[str] = "",
    organization_name: Optional[str] = ""
) -> str | List[dict] | None:
    person_name: str = normalize_string(person_name)
    employee_code: str = normalize_string(employee_code)
    organization_id: str = normalize_string(organization_id)
    organization_name: str = normalize_string(organization_name)

    data: List[dict] = get_personal_information(
        url,
        session_id,
        person_name,
        employee_code,
        organization_id,
        organization_name
    ).get("data", [])

    if len(data) == 1:
        return data[0].get("employee_code", "")
    return data

def get_personal_information(
    url: str,
    session_id: str,
    person_name: str,
    employee_code: Optional[str] = "",
    organization_id: Optional[str] = "",
    organization_name: Optional[str] = ""
) -> dict:
    # call api
    data = {
        "type": "function_calling",
        "message": {
            "name": "amiscontact@report#request_contact",
            "natural_name": "",
            "params": [
                {
                    "name": "fullName",
                    "text": person_name,
                    "value": person_name
                },
                {
                    "name": "employeeCode",
                    "text": employee_code,
                    "value": employee_code
                },
                {
                    "name": "ConfirmedOrgID",
                    "text": organization_id,
                    "value": organization_id
                },
                {
                    "name": "OrganizationUnitName",
                    "text": organization_name,
                    "value": organization_name
                },
                {
                    "name": "OrgConfirm",
                    "text": 0 if organization_id else 1,
                    "value": 0 if organization_id else 1
                },
                {
                    "name": "OrgLimit",
                    "text": "",
                    "value": 3
                },
                {
                    "name": "OrgMinThreshold",
                    "text": "",
                    "value": 0.3
                },
                {
                    "name": "OrgMarginThreshold",
                    "text": "",
                    "value": 0.1
                }
            ],
            "category": "report"
        }
    }
    status_code, body, api_log = call_api(url, session_id, data)

    # parse outputs
    data: list[dict] = []
    if status_code == 200:
        body: dict = json.loads(body)
        for item in body.get("payload") or []:
            data.append({
                "person_name": item.get("person_name"),
                "person_id": item.get("person_id"),
                "job_position": item.get("job_position"),
                "gender": item.get("gender"),
                "employee_code": item.get("employee_code")
            })

    return {
        "data": data
    }

def normalize_string(s: str) -> str:
    return s.strip()