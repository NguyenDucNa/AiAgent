from pydantic import Field, BaseModel
from langchain_core.tools import tool
from src.config import settings
import re
import requests
import json


class Input(BaseModel):
    phone_number: str = Field(
        ...,
        description="Số điện thoại của khách hàng"
    )
    email: str = Field(
        ...,
        description="Email của khách hàng"
    )


@tool("MisaCrmSearchPhoneNumber", args_schema=Input, return_direct=False)
def MisaCrmSearchPhoneNumber(
    phone_number: str,
    email: str,
):
    """Sử dụng tools này để tìm kiếm thông tin khách hàng trên CRM Misa bằng số điện thoại và email"""
    print(" ====================== MisaCrmSearchPhoneNumber ===================")

    # 1. Kiểm tra tính hợp lệ của số điện thoại và email
    phone_pattern = r"^(0[235789][0-9]{8}|02[0-9]{8,9})$"
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    is_valid = False
    if phone_number and re.match(phone_pattern, phone_number):
        is_valid = True
    if email and re.match(email_pattern, email):
        is_valid = True

    if not is_valid:
        return {
            "result": "error",
            "message": "Số điện thoại/mail bạn nhập không đúng định dạng. Vui lòng kiểm tra lại.",
        }

    # 2. Gọi API để lấy thông tin khách hàng
    try:
        url = "https://testopenapimisajsc.amis.vn/v1/api/ava/validate/info"
        headers = {
            "x-clientId": "AVA",
            "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
            "Content-Type": "application/json",
        }
        json_data = {
            "Mobile": phone_number,
            "Email": email,
        }

        response = requests.post(url, headers=headers, data=json.dumps(json_data))
        status_code = response.status_code

        if status_code != 200:
            return {
                "result": "error",
                "message": "Xin lỗi, hiện tại không thể lấy được thông tin này.",
            }

        # 3. Xử lý kết quả từ API
        body = response.json()

        if not body:
            return {
                "result": "error",
                "message": "Không tồn tại số điện thoại/email trên hệ thống CRM.",
                "data": [],
            }

        check_in_crm = None
        data = []


        if "Type" in body:
            if body["Type"] == 8:
                # Trường hợp không tồn tại trong CRM
                check_in_crm = "False"
                data = {}
                message = "Không tồn tại số điện thoại/email trên hệ thống CRM."

                # Thêm logic xử lý trực tiếp
                relevant_functions = [
                    {"name": "Thêm liên hệ", "alias": "Thêm liên hệ"},
                    {"name": "Thêm khách hàng", "alias": "Thêm khách hàng"}
                ]

                return {
                    "result": check_in_crm,
                    "message": message,
                    "data": {
                        "Email": email,
                        "Number": phone_number,
                        "function_calling": {
                            "name": "",
                            "natural_name": "",
                            "params": [],
                            "category": "action",
                            "relevant_functions": relevant_functions
                        },
                    },
                }

            elif body["Type"] == 0:
                # Trường hợp tồn tại trong CRM
                check_in_crm = "True"
                data = body.get("Data", [])
                if isinstance(data, list):
                    # Sắp xếp danh sách theo tên
                    data = sorted(data, key=lambda x: x["Name"].strip())
                    relevant_functions = []
                    tax_codes = []
                    names = []

                    # Tạo danh sách các chức năng liên quan
                    for item in data:
                        if "TaxCode" in item and "Name" in item:
                            tax_codes.append(item["TaxCode"])
                            names.append(item["Name"])
                            relevant_functions.append(
                                {"name": f"{item['Name']} - {item['TaxCode']}", "alias": f"{item['Name']} - {item['TaxCode']}"}
                            )

                    # Tạo dictionary kết quả
                    combined = list(zip(names, tax_codes))
                    sorted_combined = sorted(combined, key=lambda x: x[0])  # Sắp xếp theo tên
                    sorted_names, sorted_tax_codes = zip(*sorted_combined)
                    result_dict = {index: {"Name": name, "TaxCode": tax_code} for index, (name, tax_code) in enumerate(zip(sorted_names, sorted_tax_codes))}

                message = "Số điện thoại/email tồn tại trên hệ thống CRM, bạn có thể chọn các tính năng sau."

                return {
                    "result": check_in_crm,
                    "message": message,
                    "data": {
                        "data": result_dict,
                        "function_calling": {
                            "name": "",
                            "natural_name": "",
                            "params": [],
                            "category": "action",
                            "relevant_functions": relevant_functions
                        },
                    },
                }
            
    
        return {
            "result": "error",
            "message": "Không tồn tại số điện thoại/email trên hệ thống CRM.",
            "data": [],
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "result": "error",
            "message": "Đã xảy ra lỗi trong quá trình gọi API.",
        }