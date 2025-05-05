import requests
import traceback
from pydantic import Field, BaseModel
from typing import List, Optional, Annotated
from enum import Enum

from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState

from src.config import settings

class Input(BaseModel):
    user_query: str = Field(
        ...,
        description="Tin nhắn của người dùng"
    )
    debit_account: str = Field(
        description="Tài khoản ghi Nợ (đi với tài khoản có)",
        default=""
    )
    credit_account: str = Field(
        description="Tài khoản ghi Có (đi với tài khoản nợ)",
        default=""
    )
    bank_account: str = Field(
        description="Tài khoản ngân hàng để thực hiện giao dịch (nếu có)",
        default=""
    )
    current_time: str = Field(
        ...,
        description="Thời gian hiện tại (định dạng DD/MM/YYYY HH:MM:SS)",
    )

@tool("CreateAccountingVoucher", args_schema=Input, return_direct=False)
def CreateAccountingVoucher(
    user_query: str,
    debit_account: str = "",
    credit_account: str = "",
    bank_account: str = "",
    current_time: str = "",
    state: Annotated[dict, InjectedState] = None,
    config_params: RunnableConfig = None
):
    """Sử dụng tools này để màn hình các form chức năng trên phần mềm:
- Tạo chứng từ kế toán
- Tạo phiếu thu / phiếu chi
- Tạo phiếu thanh toán
- Tạo phiếu kế toán
- Hạch toán thuế, chứng từ.
Thông tin về tài khoản ghi nợ, tài khoản có, tài khoản ngân hàng không bắt buộc. Không yêu cầu người dùng cung cấp thông tin này."""

    try:
        API_KEY = settings.WORKFLOWS.get("accounting_voucher", "")

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        json_data = {
            "inputs": {
                "user_query": user_query,
                "debit_account": debit_account,
                "credit_account": credit_account,
                "bank_account": bank_account,
                "current_time": current_time
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
        print(f"Error while creating accounting voucher: {e}")
        traceback.print_exc()
        return {
            "is_error": True,
            "message": f"Có lỗi xảy ra khi tạo chứng từ kế toán, vui lòng thử lại sau. {e}"
        }
