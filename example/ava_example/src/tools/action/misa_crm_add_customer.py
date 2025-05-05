from pydantic import Field, BaseModel
from langchain_core.tools import tool
import re
import requests
import json
from langchain_core.runnables import RunnableConfig


class Input(BaseModel):
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
    tax_code: str = Field(
        ...,
        description="Mã số thuế của khách hàng"
    )
    customer_name: str = Field(
        ...,
        description="Tên của khách hàng"
    )
    customer_advice_status: str = Field(
        ...,
        description="Trạng thái tư vấn của khách hàng"
    )
    customer_industry: str = Field(
        ...,
        description="Ngành nghề của khách hàng"
    )
    customer_address: str = Field(
        ...,
        description="Địa chỉ của khách hàng"
    )


@tool("MisaCrmAddCustomer", args_schema=Input, return_direct=False)
def MisaCrmAddCustomer(
    latest_chatbot_response: str,
    Email: str,
    phone_number: str,
    tax_code: str,
    customer_name: str,
    customer_advice_status: str,
    customer_industry: str,
    customer_address: str,
    # config_params: RunnableConfig = None
):
    """Sử dụng để thêm khách hàng vào hệ thống, khách hàng có thể là công ty hoặc cá nhân. Các trường thông tin Mã số thuế, email, số điện thoại chỉ cần 1 trường có giá trị là được"""
    print(" ====================== MisaCrmAddCustomer ===================")

    user_id = "05484619-0cee-4998-94f1-a4228cd430af"

    url = "https://testopenapimisajsc.amis.vn/v1/api/ava/validate/permission"
    headers = {
        "x-clientId": "AVA",
        "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
        "Content-Type": "application/json",
    }

    json_data = {
        "LayoutCode": "Account",
        "EmployeeID": user_id,
        "State": "2"
    }

    try:
        # Gửi yêu cầu POST đến API
        response = requests.post(url, headers=headers,
                                 data=json.dumps(json_data))
        status_code = response.status_code
        body = response.text  # Lấy nội dung phản hồi từ API dưới dạng chuỗi JSON
        print(f"kakakakakakakakakakakakaka")
        print(f"status_code: {status_code}")
        print(f"body: {body}")
        # Tích hợp logic từ hàm main
        if status_code == 200:
            data = json.loads(body)
            if data.get("Code") == 200:
                type_value = data.get("Type")
                if type_value == 9:
                    # Trường hợp không có quyền thêm khách hàng
                    return {
                        "result": "Bạn không có quyền thêm Khách hàng. Vui lòng liên hệ quản trị hệ thống để cấp quyền"
                    }
                elif type_value == 0:
                    # Trường hợp type = 0, gọi hàm handle_type_zero
                    return handle_type_zero(
                        Code=data.get("Code"),
                        Name=customer_name,
                        Address=customer_address,
                        Status=customer_advice_status,
                        Industry=customer_industry,
                        phone_number=phone_number,
                        Email=Email,
                        tax_code=tax_code
                    )
                else:
                    # Trả về kết quả thành công với type khác 9
                    return {"result": int(type_value)}
            else:
                raise ValueError(f"Invalid code in body: {data.get('Code')}")
        else:
            raise ValueError(f"Invalid status_code: {status_code}")

    except Exception as e:
        # Xử lý ngoại lệ
        print(f"Error occurred: {e}")
        return {
            "result": "error",
            "message": str(e)
        }


def handle_type_zero(
    Code: int,
    Name: str,
    Address: str,
    Status: str,
    Industry: str,
    phone_number: str,
    Email: str,
    tax_code: str
) -> dict:
    """Xử lý logic khi type = 0"""
    check_tax_code = "True"
    if not tax_code:
        check_tax_code = "False"
        try:
            tax_code_url = "https://testopenapimisajsc.amis.vn/v1/api/ava/taxcode-info"
            headers = {
                "x-clientId": "AVA",
                "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
                "Content-Type": "application/json",
            }
            params = {"taxcode": tax_code}

            # Gửi yêu cầu GET đến API
            response = requests.get(
                tax_code_url, headers=headers, params=params)
            status_code = response.status_code
            body = response.text

            # Tích hợp gọi hàm process_api_response
            api_response = process_api_response(status_code, body, tax_code)
            if api_response["flow"] != 2:  # Kiểm tra flow để xử lý các trường hợp khác
                return {
                    "result": api_response["message"],
                    "data": api_response["data"]
                }

            if status_code == 200:
                tax_data = json.loads(body)
                if tax_data.get("Code") == 200:
                    # Mã số thuế hợp lệ, cập nhật check_tax_code
                    check_tax_code = "True"
                else:
                    # Mã số thuế không hợp lệ
                    return {
                        "result": "Mã số thuế không hợp lệ. Vui lòng kiểm tra lại."
                    }
            else:
                return {
                    "result": f"Lỗi khi gọi API kiểm tra mã số thuế: {status_code}"
                }
        except Exception as e:
            return {
                "result": f"Đã xảy ra lỗi khi kiểm tra mã số thuế: {str(e)}"
            }
    data = {
        "name": "crm_add",
        "natural_name": "",
        "params": [
            {
                "name": "LayoutCode",
                "value": "Account"
            },
            {
                "name": "Code",
                "value": Code if Code else ""
            },
            {
                "name": "Name",
                "value": Name if Name else ""
            },
            {
                "name": "Address",
                "value": Address if Address else ""
            },
            {
                "name": "Status",
                "value": Status if Status else ""
            },
            {
                "name": "Industry",
                "value": Industry if Industry else ""
            },
            {
                "name": "Mobile",
                "value": phone_number if phone_number else ""
            },
            {
                "name": "Email",
                "value": Email if Email else ""
            },
        ],
        "category": "action"
    }
    return {
        "crm_add": data,
        "check_tax_code": check_tax_code
    }

def process_api_response(status_code: int, body: str, tax_code: str) -> dict:
    """Xử lý phản hồi từ API sau khi gọi"""
    flow = 2
    data = None
    message = f"Khách hàng có mã số thuế {tax_code} đã tồn tại trên hệ thống CRM. Bạn có cần hỗ trợ gì thêm không?"
    
    if status_code == 200:
        res = json.loads(body)
        data = res.get("Data")
        if isinstance(data, dict):
            data = [data]
        if res.get("Type") == 2 or res.get("Type") == 1:
            flow = 2
            data = [{"message": "MST/mã ngân sách không tồn tại trên CRM"}]
        elif res.get("Type") == 99:
            flow = 99
            data = [{"message": "Có lỗi xảy ra khi tra cứu MST"}]
        elif res.get("Type") == 3:
            flow = 3
        elif res.get("Type") == 4:
            flow = 4
        elif res.get("Type") == 5:
            flow = 5
        elif res.get("Type") == 6:
            flow = 6
        elif res.get("Type") == 7:
            flow = 7
        else:
            flow = 10
            data = [{}]
    else:
        message = f"Lỗi HTTP: {status_code}"

    return {
        "data": data,
        "flow": flow,
        "message": message
    }

