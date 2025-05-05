import json
import requests
from pydantic import BaseModel, Field
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import InjectedState
from typing import Optional, Annotated

# Định nghĩa các tham số Agent cần truyền vào khi gọi Tool (sử dụng BaseModel của thư viện Pydantic)
class GetBirthDayInput(BaseModel):
    from_date: str = Field(
        ..., # Dấu ... có nghĩa là tham số này là bắt buộc
        description="Ngày bắt đầu (dd/mm/yyyy) của khoảng thời gian lấy thông tin sinh nhật. Mặc định là ngày hôm nay nếu không được cung cấp."
    )
    to_date: str = Field(
        ..., # Dấu ... có nghĩa là tham số này là bắt buộc
        description="Ngày kết thúc (dd/mm/yyyy) của khoảng thời gian lấy thông tin sinh nhật. Mặc định là ngày hôm nay nếu không được cung cấp."
    )
    organization_name: Optional[str] = Field(
        description="Retrieve data based on the exact organization/product/project name as provided by the user (e.g., khối sản xuất, khối kinh doanh, sản phẩm ..., dự án...). Ignore this parameter if the organization ID is available or if the organization is MISA company.",
        default=""
    )
    organization_id: Optional[str] = Field(
        description="Organization ID (UUID). Must include if available",
        default=""
    )
    job_title: Optional[str] = Field(
        description="Chức vụ (bằng tiếng Việt, ví dụ: lập trình viên, tư vấn viên) để lọc kết quả.",
        default=""
    )


@tool("GetBirthDay", args_schema=GetBirthDayInput)
def GetBirthDay(
    from_date: str = "",
    to_date: str = "",
    organization_name: str = "",
    organization_id: str ="",
    job_title: str = "",
    send_wish_request: bool = False,
    contains_birthday_wish: bool = False,
    state: Annotated[dict, InjectedState] = None, # Thêm dòng này nếu muốn tool có thể truy cập vào state
    config_param: RunnableConfig = None, # Thêm dòng này nếu muốn tool có thể truy cập vào config_param
) -> str:
    """Sử dụng để lấy danh sách những người sinh nhật trong một khoảng thời gian nhất định, của một phòng ban trong công ty"""
    
    user_id = config_param["configurable"].get("user_id", "")

    return {
        "function_calling": {
            "name": "action#GetBirthDay",
            "natural_name": "Lấy thông tin sinh nhật của một nhân viên",
            "params": {
                "user_id": user_id,
                "from_date": from_date,
                "to_date": to_date,
                "organization_name": organization_name,
                "organization_id": organization_id,
                "job_title": job_title,
                "send_wish_request": send_wish_request,
                "contains_birthday_wish": contains_birthday_wish
            },
            "category": "action",
        }
    }

