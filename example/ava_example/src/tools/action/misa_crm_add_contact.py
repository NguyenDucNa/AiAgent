from pydantic import Field, BaseModel
from langchain_core.tools import tool
from src.config import settings
import requests
import json


class Input(BaseModel):
    user_id: str = Field(
        ...,
        description="ID của người dùng"
    )
    latest_chatbot_response: str = Field(
        ...,
        description="tin nhắn tước đó của người dùng"
    )
    Email: str = Field(
        ...,
        description="Email của khách hàng"
    )  
    phone_number: str = Field(
        ...,
        description="Số điện thoại của khách hàng"
    )


@tool("MisaCrmAddContact", args_schema=Input, return_direct=False)
def MisaCrmAddContact(
    user_id: str,
    latest_chatbot_response: str,
    Email: str,
    phone_number: str
):
    """Sử dụng tools này để thêm liên hệ vào CRM Misa"""
    print(" ====================== MisaCrmAddContact ===================")

    url = "https://testopenapimisajsc.amis.vn/v1/api/ava/validate/permission"
    headers = {
        "x-clientId": "AVA",
        "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
        "Content-Type": "application/json",
    }

    json_data = {
        "LayoutCode": "Contact",
        "EmployeeID": user_id,
        "State": "2"
    }

    try:
        # Gửi yêu cầu POST đến API
        response = requests.post(url, headers=headers, data=json.dumps(json_data))
        status_code = response.status_code
        body = response.text  # Lấy nội dung phản hồi từ API dưới dạng chuỗi JSON

        if status_code == 200:
            # Parse JSON body
            data = json.loads(body)

            # Kiểm tra "Code" trong phản hồi
            if data.get("Code") == 200:
                # Lấy giá trị "Type" từ phản hồi
                type_value = data.get("Type")

                # Tích hợp logic cho từng giá trị của "Type"
                if type_value == 0:
                    # Logic khi result = 0
                    crm_add_data = {
                        "name": "crm_add",
                        "natural_name": "",
                        "params": [
                            {
                                "name": "LayoutCode",
                                "value": "Contact"
                            },
                            {
                                "name": "Email",
                                "value": Email if Email else ""
                            },
                            {
                                "name": "Mobile",
                                "value": phone_number if phone_number else ""
                            }
                        ],
                        "category": "action"
                    }
                    return {
                        "result": "success",
                        "message": "Thêm khách hàng thành công",
                        "data": {
                            "crm_add": crm_add_data
                        }
                    }

                elif type_value == 9:
                    # Logic khi result = 9
                    return {
                        "result": "error",
                        "message": "Bạn không có quyền thêm Khách hàng. Vui lòng liên hệ quản trị hệ thống để cấp quyền",
                    }

                else:
                    # Trường hợp khác
                    return {
                        "result": "error",
                        "message": f"Không xác định được hành động với Type: {type_value}",
                    }
            else:
                # Trường hợp "Code" không phải 200
                return {
                    "result": "error",
                    "message": f"Invalid code in body: {data.get('Code')}",
                }
        else:
            # Trường hợp status_code không phải 200
            return {
                "result": "error",
                "message": f"Invalid status_code: {status_code}",
            }

    except Exception as e:
        # Xử lý ngoại lệ
        print(f"Error occurred: {e}")
        return {
            "result": "error",
            "message": "Đã xảy ra lỗi trong quá trình gọi API.",
        }