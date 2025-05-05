

from pydantic import Field, BaseModel
from langchain_core.tools import tool
from src.config import settings
from enum import Enum


class ActionType(Enum):
    A = "Thêm khách hàng"
    B = "Thêm cơ hội"


class Input(BaseModel):
    action: ActionType = Field(description="chức năng thực thi thành công")


@tool("MisaCrmActionSuccess", args_schema=Input, return_direct=False)
def MisaCrmActionSuccess(action: ActionType):
    """
    Chỉ được sử dụng khi nhân được thông báo người dùng "Hệ thống thêm Khách hàng thành công"
    """
    if action == ActionType.A:
        return {
            "answer": "Đã thêm khách hàng thành công. Bạn có muốn hỗ trợ gì thêm không?",
            "function_calling": {
                "name": "",
                "natural_name": "",
                "params": [],
                "category": "action",
                "relevant_functions": [{"name": "Thêm cơ hội", "alias": "Thêm cơ hội"}]
            },
        }

    elif action == ActionType.B:
        return {
            "answer": "Bạn có muốn hỗ trợ gì thêm không?",
        }  
    


    