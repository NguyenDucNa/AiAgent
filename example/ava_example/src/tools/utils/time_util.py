from datetime import datetime, timedelta
import pytz

__all__ = [
    "get_current_time",
    "get_this_week_time",
    "get_current_date"
]

def get_current_time() -> str:
    now = datetime.now(pytz.timezone("Asia/Ho_Chi_Minh"))
    if now.weekday() < 6:
        weekday = f"thứ {now.weekday() + 2}"
    else:
        weekday = "chủ nhật"

    current_time = f"{weekday}, ngày {now.day:02d}/{now.month:02d}/{now.year}"
    return current_time

def get_this_week_time() -> dict:
    now = datetime.now(pytz.timezone("Asia/Ho_Chi_Minh"))

    monday = now - timedelta(now.weekday() - 0)
    monday = f"ngày {monday.day:02d}/{monday.month:02d}/{monday.year}"

    sunday = now + timedelta(6 - now.weekday())
    sunday = f"ngày {sunday.day:02d}/{sunday.month:02d}/{sunday.year}"
    return {
        "monday": monday,
        "sunday": sunday
    }