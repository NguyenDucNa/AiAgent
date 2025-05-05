
from pydantic import Field, BaseModel
from langchain_core.tools import tool
import re
import requests
import json
from langchain_core.runnables import RunnableConfig


class Input(BaseModel):
    code: str = Field(
        ...,
        description="Mã số thuế của khách hàng"
    )
    Name: str = Field(
        ...,
        description="Tên công ty"
    )
    Address: str = Field(
        ...,
        description="Địa chỉ công ty"
    )
    Status: str = Field(
        ...,
        description="Tinh trạng công ty"
    )
    user_id: str = Field(
        ...,
        description="ID của người dùng"
    )
    Industry: str = Field(
        ...,
        description="Ngành nghề của công ty"
    )


@tool("MisaCrmAddOpportunity", args_schema=Input, return_direct=False)
def MisaCrmAddOpportunity(
    code: str,
    Name: str,
    Address: str,
    user_id: str,
    Industry: str,
    Status: str,
):
    """Sử dụng để thêm cơ hội vào hệ thống, khách hàng có thể là công ty hoặc cá nhân sau khi đã thêm khách hàng thành công"""
    print(" ====================== MisaCrmAddOpportunity==========")

    user_id = "05484619-0cee-4998-94f1-a4228cd430af"

    url = "https://testopenapimisajsc.amis.vn/v1/api/ava/validate/permission"
    headers = {
        "x-clientId": "AVA",
        "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
        "Content-Type": "application/json",
    }

    json_data = {
        "LayoutCode": "opportunity",
        "EmployeeID": user_id,
        "ID": "8660208",
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
                        "result": "Bạn không có quyền thêm cơ hội. Vui lòng liên hệ quản trị hệ thống để cấp quyền"
                    }
                elif type_value == 0:
                    # Trường hợp type = 0, gọi hàm handle_type_zero
                    return handle_type_zero(
                        user_id=user_id,
                        Code=code,
                        Name=Name,
                        Address=Address,
                        Status=Status,
                        Industry=Industry,
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
    Code: str,
    Name: str,
    Address: str,
    Status: str,
    user_id: str,
    Industry: str,
) -> dict:
    """Xử lý logic khi type = 0"""
    check_tax_code = "True"
    if not Code:
        check_tax_code = "False"
        try:
            tax_code_url = "https://testopenapimisajsc.amis.vn/v1/api/ava/account/info/"
            headers = {
                "x-clientId": "AVA",
                "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
                "Content-Type": "application/json",
            }
            params = {"taxcode": Code}

            # Gửi yêu cầu GET đến API
            response = requests.get(    
                tax_code_url, headers=headers, params=params)
            status_code = response.status_code
            body = response.text

            # Tích hợp logic từ hàm main
            data = json.loads(body)
            data_info = data.get("Data", {})

            message = ""
            if not data_info:
                message = "Không tìm thấy thông tin KH"
                data_info = [{}]
            if isinstance(data_info, dict):
                data_info = [data_info]

            first_entry = data_info[0]

            # Extract fields from the first entry in Data
            account_id = first_entry.get("ID", "")
            account_name = first_entry.get("AccountName", "Unknown")
            layout_code = first_entry.get("LayoutCode", "Opportunity")
            tax_code = first_entry.get("TaxCode", "Unknown")

            if account_id:
                # Define the parameters safely
                params = [
                    {
                        "name": "LayoutCode",
                        "value": "Opportunity"
                    },
                    {
                        "name": "AccountID",
                        "value": account_id
                    },
                    {
                        "name": "AccountName",
                        "value": account_name
                    },
                    {
                        "name": "TaxCode",
                        "value": tax_code
                    }
                ]
                function_calling = {
                    "name": "crm_add",
                    "natural_name": "",
                    "params": params,
                    "category": "action"
                }
            else:
                function_calling = {}

            # Return extracted information
            return {
                "function_calling": function_calling,
                "message": message
            }

        except Exception as e:
            return {
                "result": f"Đã xảy ra lỗi khi kiểm tra mã số thuế: {str(e)}"
            }

