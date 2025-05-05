import requests
import traceback
from pydantic import Field, BaseModel
from typing import List, Optional, Annotated
from enum import Enum

from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState

from example.ava_example.src.config import settings

class Input(BaseModel):
    user_query: str = Field(
        ...,
        description="Tin nhắn của người dùng"
    )
    start_date: str = Field(
        description="Ngày bắt đầu kỳ báo cáo (định dạng DD/MM/YYYY). Mặc định là ngày đầu tháng hiện tại",
        default=""
    )
    end_date: str = Field(
        description="Ngày kết thúc kỳ báo cáo (định dạng DD/MM/YYYY). Mặc định là ngày cuối tháng hiện tại",
        default=""
    )
    current_month: str = Field(
        ...,
        description="Tháng hiện tại (định dạng MM)"
    )
    current_year: str = Field(
        ...,
        description="Năm hiện tại (định dạng YYYY)"
    )

@tool("CreateFinancialReport", args_schema=Input, return_direct=True)
def CreateFinancialReport(
    user_query: str,
    start_date: str = "",
    end_date: str = "",
    current_month: str = "",
    current_year: str = "",
    state: Annotated[dict, InjectedState] = None,
    config_params: RunnableConfig = None
):
    """Sử dụng tools này để mở màn hình form chức năng trên màn hình phần mềm:
- Lập báo cáo tài chính
- Tạo thuyết minh báo cáo tài chính
- Lập báo cáo tài chính tổng hợp
- Tạo thuyết minh báo cáo tài chính tổng hợp
- Lập báo cáo tài chính giữa niên độ
- Tạo thuyết minh báo cáo tài chính giữa niên độ
Nếu ngươi dùng không nhắc đến thời điểm bắt đầu và kết thúc kỳ báo cáo thì tự hiểu là ngày đầu và cuối tháng hiện tại, không hỏi lại người dùng"""

    try:
        API_KEY = settings.WORKFLOWS.get("create_financial_report", "")

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        json_data = {
            "inputs": {
                "user_query": user_query,
                "organization": "",
                "start_date": start_date,
                "end_date": end_date,
                "use_case": "Báo cáo tài chính, thuyết minh báo cáo tài chính",
                "current_month": current_month,
                "current_year": current_year
            },
            "response_mode": "blocking",
            "user": "multi-agent"
        }

        response = requests.post(
            url=settings.WORKFLOW_URL,
            headers=headers,
            json=json_data
        )

        if response.status_code != 200:
            return response.json()
        else:
            results: dict = response.json().get("data", {}).get("outputs", {})
            return results

    except Exception as e:
        print(f"Error while creating financial report: {e}")
        traceback.print_exc()
        return {
            "is_error": True,
            "message": f"Có lỗi xảy ra khi tạo báo cáo tài chính, vui lòng thử lại sau. {e}"
        }
