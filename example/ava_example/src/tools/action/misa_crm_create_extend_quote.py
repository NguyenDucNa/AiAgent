from product_info import ProductType, PRODUCTS, MEI_ENTERPRISE_PKG, MEI_HOUSEHOLD_PKG, RESPONSE_CREATE_EXTEND_QUOTE
from pydantic import Field, BaseModel
from langchain_core.tools import tool
from enum import Enum
import os
import sys
import requests
import json

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../../../../.."))
sys.path.append(project_root)


class Input(BaseModel):
    product_name: ProductType = Field(..., description="Tên sản phẩm")
    product_name_2: ProductType = Field(
        ..., description="Tên sản phẩm thứ hai. Nếu người dùng muốn mua 2 sản phẩm")
    product_name_3: ProductType = Field(
        ..., description="Tên sản phẩm thứ ba. Nếu người dùng muốn mua 3 sản phẩm")
    product_name_4: ProductType = Field(
        ..., description="Tên sản phẩm thứ tư. Nếu người dùng muốn mua 4 sản phẩm")
    tax_code: str = Field(..., description="Mã số thuế khách hàng")
    domain: str = Field(..., description="Tên miền của khách hàng")
    MeInvRelease_Enterprise_Pkgs: MEI_ENTERPRISE_PKG = Field(
        ..., description="Riêng với sản phẩm MeInvoice Doanh nghiệp Phát hành hóa đơn cần phải có tên gói đi kèm")
    MeInvRelease_Household_Pkgs: MEI_HOUSEHOLD_PKG = Field(
        ..., description="Riêng với sản phẩm MeInvoice Hộ kinh doanh Phát hành hóa đơn cần phải có tên gói đi kèm")
    promotion_rates: str = Field(
        ..., description="Phần trăm chiết khấu của mỗi sản phẩm. Là các số viết cách nhau bởi dấu phẩy. Viết ở dạng list trong Python. Số phần tử của list bằng số lượng sản phẩm. Ví dụ [0, 3, 5] hoặc [0, 0, 0, 4]")
    promotion_amounts: str = Field(
        ..., description="Số tiền chiết khấu của mỗi sản phẩm. Viết ở dạng List trong Python. Số phần tử của List bằng số lượng sản phẩm. Ví dụ [100000, 0, 20000]")
    company: str = Field(..., description="Tên công ty khách hàng")


@tool("MisaCrmCreateExtendQuote", args_schema=Input, return_direct=False)
def MisaCrmCreateExtendQuote(
    product_name: ProductType,
    product_name_2: ProductType,
    product_name_3: ProductType,
    product_name_4: ProductType,
    tax_code: str,
    domain: str,
    MeInvRelease_Enterprise_Pkgs: MEI_ENTERPRISE_PKG,
    MeInvRelease_Household_Pkgs: MEI_HOUSEHOLD_PKG,
    promotion_rates: str,
    promotion_amounts: str,
    company: str
):
    """
    "Sử dụng để tạo báo giá gia hạn sản phẩm trên MISA_Store. Thông tin tối thiểu cần có khi tạo báo giá là tên sản phẩm và 1 trong 2 thông tin mã số thuế hoặc domain khách hàng. Riêng với sản phẩm "MeInvoice Doanh nghiệp - Phát hành hóa đơn" và "MeInvoice Hộ kinh doanh - Phát hành hóa đơn" thì cần có tên gói kèm theo"
    """
    print(" ====================== MisaCrmCreateExtendQuote ===================")
#     if not tax_code or not domain:
#         return {
#             "result": "Thông báo cho người dùng thông cần tối thiểu thông tin MST hoặc Domain"
#         }

#     try:
#         response = type('MockResponse', (), {
#             'status_code': RESPONSE_CREATE_EXTEND_QUOTE['status_code'],
#             'text': RESPONSE_CREATE_EXTEND_QUOTE['body'],
#             'json': lambda self: {'body': json.loads(RESPONSE_CREATE_EXTEND_QUOTE['body'])}
#         })()

#         print(f"API call status code: {response.status_code}")

#         if response.status_code == 200:
#             response_data = response.json()

#             # Process the response with the new logic
#             if not domain:
#                 domain = ""
#             if not tax_code:
#                 tax_code = ""

#             body = RESPONSE_CREATE_EXTEND_QUOTE['body']
#             status_code = RESPONSE_CREATE_EXTEND_QUOTE['status_code']

#             if status_code == 200:
#                 PRODUCTS = json.loads(body)

#             product_list = [product_name, product_name_2,
#                             product_name_3, product_name_4]
#             promotion_rates = eval(promotion_rates)
#             promotion_amounts = eval(promotion_amounts)

#             lack_packages = ""
#             for product in product_list:
#                 if product == "meInvoice Doanh nghiệp - Phát hành hóa đơn":
#                     if not MeInvRelease_Enterprise_Pkgs:
#                         lack_packages += "Khách hàng cần cung cấp tên gói cho sản phẩm meInvoice Doanh nghiệp - Phát hành hóa đơn\n"
#                 elif product == "meInvoice Hộ Kinh doanh - Phát hành hóa đơn":
#                     if not MeInvRelease_Household_Pkgs:
#                         lack_packages += "Khách hàng cần cung cấp tên gói cho sản phẩm meInvoice Hộ Kinh doanh - Phát hành hóa đơn\n"

#             request_bodys = []
#             for product_name, promotion_rate, promotion_amount in zip(product_list, promotion_rates, promotion_amounts):
#                 for product in PRODUCTS:
#                     if product["AppName"] == product_name and product["AppName"] == "meInvoice Doanh nghiệp - Phát hành hóa đơn":
#                         product_info = product
#                         request_body = {
#                             "AppCode": product_info["AppCode"],
#                             "ProductId": product_info["ProductID"],
#                             "IsExtend": True,
#                             "TaxCode": tax_code,
#                             "CompanyName": company,  # Using company instead of company_name as per parameter name
#                             "domain": domain,
#                             "PromotionRate": promotion_rate,
#                             "PromotionAmount": promotion_amount,
#                             "OrderItemInfos": [
#                                 {
#                                     "DisplayName": MeInvRelease_Enterprise_Pkgs,
#                                     "Quantity": 1,
#                                     "ModuleName": "",
#                                 }
#                             ]
#                         }
#                         request_bodys.append(request_body)
#                     elif product["AppName"] == product_name and product["AppName"] == "meInvoice Hộ Kinh doanh - Phát hành hóa đơn":
#                         product_info = product
#                         request_body = {
#                             "AppCode": product_info["AppCode"],
#                             "ProductId": product_info["ProductID"],
#                             "IsExtend": True,
#                             "TaxCode": tax_code,
#                             "CompanyName": company,  # Using company instead of company_name
#                             "domain": domain,
#                             "PromotionRate": promotion_rate,
#                             "PromotionAmount": promotion_amount,
#                             "OrderItemInfos": [
#                                 {
#                                     "DisplayName": MeInvRelease_Household_Pkgs,
#                                     "Quantity": 1,
#                                     "ModuleName": "",
#                                 }
#                             ]
#                         }
#                         request_bodys.append(request_body)
#                     elif product["AppName"] == product_name:
#                         product_info = product
#                         request_body = {
#                             "AppCode": product_info["AppCode"],
#                             "ProductId": product_info["ProductID"],
#                             "IsExtend": True,
#                             "TaxCode": tax_code,
#                             "CompanyName": company,  # Using company instead of company_name
#                             "domain": domain,
#                             "PromotionRate": promotion_rate,
#                             "PromotionAmount": promotion_amount
#                         }
#                         request_bodys.append(request_body)

#             request_bodys = json.dumps(request_bodys, ensure_ascii=False)
#             print(f"Request bodies: {request_bodys}")
#             if not lack_packages:
#                 return lack_packages_empty(request_bodys)
#             else:
#                 return {
#                     "lack_packages": lack_packages,
#                     "request_bodys": request_bodys,
#                 }

#         else:
#             print(f"Request failed with status code: {response.status_code}")
#             return {"Thông báo cho người dùng hệ thống đang lỗi không sinh được đơn hàng gia hạn."}
#     except requests.exceptions.RequestException as e:
#         print(f"API call failed: {e}")
#         return {"error": f"API call failed: {str(e)}"}


# def lack_packages_empty(request_bodys):
#     print(request_bodys)
#     try:
#         # Gọi API lấy thông tin báo giá
#         quote_api_url = "http://teststore.misatest.local:10001/api/Quotes/GetQuoteInfos"
#         quote_headers = {
#             'Content-Type': 'application/json'
#         }
        
    
#         quote_payload = {
#             "requestBodies": json.loads(request_bodys)  # Giả sử request_bodys được truyền từ hàm chính
#         }
        
#         print(f"Gọi API báo giá từ hàm lack_packages_empty: {quote_api_url}")
#         quote_response = requests.post(
#             quote_api_url, 
#             headers=quote_headers, 
#             json=quote_payload,
#             timeout=30
#         )
        
#         print(f"Kết quả gọi API báo giá: {quote_response.status_code}")
        
#         if quote_response.status_code == 200:
#             quote_data = quote_response.json()
#             return {
#                 "result": "Tạo báo giá gia hạn thành công",
#                 "quote_info": quote_data
#             }
#         else:
#             print(f"Lỗi khi gọi API báo giá: {quote_response.status_code}")
#             return {
#                 "result": "Thông báo cho người dùng hệ thống đang lỗi không sinh được đơn hàng gia hạn.",
#                 "error": f"Lỗi khi gọi API báo giá: {quote_response.status_code}"
#             }
#     except Exception as e:
#         print(f"Lỗi khi gọi API báo giá: {e}")
#         return {
#             "result": "Thông báo cho người dùng hệ thống đang lỗi không sinh được đơn hàng gia hạn.",
#             "error": f"Lỗi khi gọi API báo giá: {str(e)}"
#         }

# code này để call api thẳng tới tool, ko cần chuyển j
    try:
        url = 'https://test-aiservice.misa.com.vn/v1/workflows/run'
        api_key = "app-khLKWqdmeNS1nrkMRkroJ8hP"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        json_data = {
            "inputs": {
                "product_name": product_name.value,
                "product_name_2": product_name_2.value,
                "product_name_3": product_name_3.value,
                "product_name_4": product_name_4.value,
                "tax_code": tax_code,
                "domain": domain,
                "MeInvRelease_Enterprise_Pkgs": MeInvRelease_Enterprise_Pkgs.value,
                "MeInvRelease_Household_Pkgs": MeInvRelease_Household_Pkgs.value,
                "promotion_rates": promotion_rates,
                "promotion_amounts": promotion_amounts,
                "company": company
            },
            "response_mode": "blocking",
            "user": "multi-agent"
        }

        response = requests.post(url, headers=headers, json=json_data)

        # For response handling
        print(response.text)
        if response.status_code == 200:
            response_data = response.json()

            # Check if the response has the outputs field
            if "outputs" in response_data:
                outputs = response_data["outputs"]

                # Format the output to include both instruction and errorMessage if available
                output_message = {}
                if "instruction" in outputs:
                    output_message["instruction"] = outputs["instruction"]
                if "errorMessage" in outputs:
                    output_message["errorMessage"] = outputs["errorMessage"]

                print(output_message)
                return output_message
            else:
                print("No outputs field in response")
                return response_data
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"API call failed: {e}")
        return {
            "result": "Có lỗi xảy ra trong quá trình tạo báo giá gia hạn"
        }


if __name__ == "__main__":
    result = MisaCrmCreateExtendQuote.invoke({
        "product_name": "MISA Quản lý tài sản",
        "product_name_2": "MISA Quản lý tài sản",
        "product_name_3": "MISA Quản lý tài sản",
        "product_name_4": "MISA Quản lý tài sản",
        "tax_code": "0110115204",       
        "domain": "test.misa.vn",
        "MeInvRelease_Enterprise_Pkgs": "MEIVE-20.000",
        "MeInvRelease_Household_Pkgs": "MEIMTT-200.000",
        "promotion_rates": "[0, 0, 0, 0]",
        "promotion_amounts": "[0, 0, 0, 0]",
        "company": "Công ty TNHH ABC"
    })
    print(result)
