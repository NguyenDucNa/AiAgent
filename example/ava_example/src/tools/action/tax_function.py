from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional, Annotated
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import InjectedState


class TaxType(Enum):
    VAT = "giá trị gia tăng"
    CIT = "thu nhập doanh nghiệp"
    SCT = "tiêu thụ đặc biệt"
    NAN = "not_mentioned"

class Input(BaseModel):
    user_query: str = Field(
        ...,
        description="Tin nhắn của người dùng"
    )
    item_name: str = Field(
        description="Tên hàng hóa, mặt hàng, ví dụ: quần áo, máy móc. Nếu người dùng không nhắc tới thì giá trị mặc định là rỗng.",
        default="",
    )
    start_date: str = Field(
        description="Ngày bắt đầu kỳ kê khai thuế (định dạng DD/MM/YYYY). Nếu lập tờ khai năm nay, tháng này, ... thì start_date là ngày đầu tiên của tháng/năm đó.",
        default="",
    )
    end_date: str = Field(
        description="Ngày kết thúc kỳ kê khai thuế (định dạng DD/MM/YYYY). Nếu lập tờ khai năm nay, tháng này, ... thì end_date là ngày cuối cùng của tháng/năm đó.",
        default=""
    )
    organtization: str = Field(
        description="Tên tổ chức. Nếu người dùng không nhắc tới thì giá trị mặc định là rỗng.",
        default=""
    )
    tax_return_type: TaxType = Field(
        ...,
        description="Loại thuế (giá trị gia tăng/thuế thu nhập doanh nghiệp/thuế tiêu thụ đặc biệt)",
    )


@tool("create_tax_declaration", args_schema=Input, return_direct=True)
def create_tax_declaration(
    user_query: str = "",
    item_name: str = "",
    start_date: str = "",
    end_date: str = "",
    organtization: str = "",
    tax_return_type: TaxType = TaxType.NAN,
    state: Annotated[dict, InjectedState] = None,
    config_params: RunnableConfig = None
) -> str:
    """Sử dụng tools này để mở màn hình các form chức năng trên phần mềm:
- Tạo tờ khai thuế giá trị gia tăng
- Tạo tờ khai thuế thu nhập doanh nghiệp
- Tạo tờ khai thuế tiêu thụ đặc biệt
- Đưa ra hướng dẫn quyết toán thuế
- Tra cứu mặt hàng giảm thuế.
Các thông tin item_name, start_date, end_date, organtization không bắt buộc."""
    
    try:
        from src.config import settings
        import requests
        import traceback
        
        API_KEY = settings.WORKFLOWS.get("tax_declaration", "")

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        json_data = {
            "inputs": {
                "user_query": user_query,
                "item_name": item_name,
                "start_date": start_date,
                "end_date": end_date,
                "organtization": organtization,
                "tax_return_type": tax_return_type.value
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
        print(f"Error while creating tax declaration: {e}")
        traceback.print_exc()
        return {
            "is_error": True,
            "message": f"Có lỗi xảy ra khi tạo tờ khai thuế, vui lòng thử lại sau. {e}"
        }
