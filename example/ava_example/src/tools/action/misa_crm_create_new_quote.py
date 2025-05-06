from product_info import ProductType, PRODUCTS, MEI_ENTERPRISE_PKG, MEI_HOUSEHOLD_PKG, RESPONSE_CREATE_EXTEND_QUOTE
from pydantic import Field, BaseModel
from typing import Optional
from langchain_core.tools import tool
from enum import Enum
import json
import requests


import os
import sys
# project_root = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), "../../../../.."))
# sys.path.append(project_root)

from src.tools.utils import openai_service


class Input(BaseModel):
    product_name: ProductType = Field(..., description="Tên sản phẩm")
    promotion_amount: int = Field(..., description="Số tiền chiết khấu của sản phẩm chính. Nếu user không cung cấp thì nhận giá trị 0")
    promotion_rate: int = Field(..., description="Phần trăm (%) chiết khấu của sản phẩm chính. Ví dụ chiết khấu 5% thì nhận giá trị 5. Nếu user không cung cấp thì nhận giá trị 0. ")

    user_query: Optional[str] = Field(None, description="Tin nhắn của người dùng")
    product_main_package: Optional[str] = Field(None, description="Tên gói chính của sản phẩm")
    product_subpackages: Optional[str] = Field(None, description="Danh sách các gói mua thêm, gói dịch vụ của sản phẩm thứ nhất, và số lượng tương ứng của mỗi gói")
    main_package_quantity: Optional[str] = Field(None, description="Số lượng gói chính, có thể tính bằng năm, tháng, gói, khóa học. VD: 2 năm, 3 gói, 1 khóa, ...")

    product_name_2: Optional[ProductType] = Field(None, description="Tên sản phẩm thứ 2, nếu người dùng muốn mua 2 sản phẩm")
    product_main_package_2: Optional[str] = Field(None, description="  Gói chính của sản phẩm thứ 2.")
    main_package_quantity_2: Optional[str] = Field(None, description="Số lượng gói chính của sản phẩm thứ 2, có thể tính bằng năm, tháng, gói, khóa học. VD: 2 năm, 3 gói, 1 khóa, ...")
    product_subpackages_2: Optional[str] = Field(None, description="Danh sách các gói mua thêm, gói dịch vụ của sản phẩm thứ 2, và số lượng tương ứng của mỗi gói")
    promotion_amount_2: Optional[int] = Field(None, description="Số tiền chiết khấu của sản phẩm thứ 2. Nếu user không cung cấp thì nhận giá trị 0")
    promotion_rate_2: Optional[int] = Field(None, description="Phần trăm (%) chiết khấu của sản phẩm thứ 2. Ví dụ chiết khấu 5% thì nhận giá trị 5. Nếu user không cung cấp thì nhận giá trị 0. ")

    product_name_3: Optional[ProductType] = Field(None, description="Tên sản phẩm thứ 3, nếu người dùng muốn mua 3 sản phẩm")
    product_main_package_3: Optional[str] = Field(None, description="Gói chính của sản phẩm thứ 3.")
    main_package_quantity_3: Optional[str] = Field(None, description="Số lượng gói chính của sản phẩm thứ 3, có thể tính bằng năm, tháng, gói, khóa học. VD: 2 năm, 3 gói, 1 khóa, ...")
    product_subpackages_3: Optional[str] = Field(None, description="Danh sách các gói mua thêm, gói dịch vụ của sản phẩm thứ 3, và số lượng tương ứng của mỗi gói")
    promotion_amount_3: Optional[int] = Field(None, description="Số tiền chiết khấu của sản phẩm thứ 3. Nếu user không cung cấp thì nhận giá trị 0")
    promotion_rate_3: Optional[int] = Field(None, description="Phần trăm (%) chiết khấu của sản phẩm thứ 3. Ví dụ chiết khấu 5% thì nhận giá trị 5. Nếu user không cung cấp thì nhận giá trị 0. ")

    product_name_4: Optional[ProductType] = Field(None, description="Tên sản phẩm thứ 4, nếu người dùng muốn mua 4 sản phẩm")
    product_main_package_4: Optional[str] = Field(None, description="Gói chính của sản phẩm thứ 4.")
    main_package_quantity_4: Optional[str] = Field(None, description="Số lượng gói chính của sản phẩm thứ 4, có thể tính bằng năm, tháng, gói, khóa học. VD: 2 năm, 3 gói, 1 khóa, ...")
    product_subpackages_4: Optional[str] = Field(None, description="Danh sách các gói mua thêm, gói dịch vụ của sản phẩm thứ 4, và số lượng tương ứng của mỗi gói")
    promotion_amount_4: Optional[int] = Field(None, description="Số tiền chiết khấu của sản phẩm thứ tư. Nếu user không cung cấp thì nhận giá trị 0")
    promotion_rate_4: Optional[int] = Field(None, description="Phần trăm (%) chiết khấu của sản phẩm thứ 4. Ví dụ chiết khấu 5% thì nhận giá trị 5. Nếu user không cung cấp thì nhận giá trị 0. ")

    Company: Optional[str] = Field(None, description="Công ty khách hàng")
    tax_code: Optional[str] = Field(None, description="Mã số thuế (MST) của khách hàng")


@tool("MisaCrmCreateNewQuote", args_schema=Input, return_direct=False)
def MisaCrmCreateNewQuote(**params):
    """
    Sử dụng để tạo báo giá mua mới sản phẩm cho khách hàng. Mỗi sản phẩm gồm 1 gói chính, không giới hạn các gói mua thêm và gói dịch vụ đi kèm (subpackages). Các gói mua thêm và gói dịch vụ đi kèm được trích xuất thành danh sách cách nhau bởi dấu ;
    Ví dụ: "Gói 1; Gói 2; Gói 3"
    """
    print(" ====================== MisaCrmCreateNewQuote ===================")
    # Phân loại các trường hợp dựa vào số lượng sản phẩm và gọi hàm tương ứng
    product_name_2 = params.get("product_name_2", "")
    product_name_3 = params.get("product_name_3", "")
    product_name_4 = params.get("product_name_4", "")

     # Xử lý case tương ứng dựa trên số lượng sản phẩm
    if not product_name_2 or product_name_2 == "":
        # Trường hợp 1: Chỉ có sản phẩm chính, các sản phẩm 2,3,4 trống
        result = handle_case1(params)
    elif (product_name_2 and product_name_2 != "") and (not product_name_3 or product_name_3 == ""):
        # Trường hợp 2: Có sản phẩm chính và sản phẩm 2, các sản phẩm 3,4 trống
        result = handle_case2(params)
    elif (product_name_2 and product_name_2 != "") and (product_name_3 and product_name_3 != "") and (not product_name_4 or product_name_4 == ""):
        # Trường hợp 3: Có sản phẩm chính, sản phẩm 2 và 3, sản phẩm 4 trống
        result = handle_case3(params)
    else:
        # Trường hợp 4: Có đủ 4 sản phẩm
        result = handle_case4(params)
    
    # Kiểm tra nếu có lỗi từ quá trình xử lý
    if "error" in result:
        return result
    
    # Gọi API với kết quả JSON từ quá trình xử lý
    quote_data = result["result"]
    api_result = call_quote_api(quote_data)
    
    # Kiểm tra kết quả API và trả về thông báo phù hợp
    if "link_to_order" in api_result:
        return {
            "link_to_order": api_result["link_to_order"],
            "instruction": api_result["instruction"]
        }
    else:
        return {
            "result": "Thông báo cho người dùng hệ thống đang lỗi không tạo được đơn hàng.",
            "details": api_result
        }

def call_quote_api(quote_data):
    """
    Gọi API CreateQuote với dữ liệu đơn hàng đã được tạo
    """
    api_url = "http://teststore.misatest.local:10001/api/Quotes/GetQuoteInfos"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(api_url, json=quote_data, headers=headers)
        
        if response.status_code == 200:
            body = response.json()
            link = body["Data"]
            return {
                "link_to_order": str(link),
                "instruction": "Gửi link báo giá tới người dùng" 
            }
        else:
            return {
                "status_code": response.status_code,
                "error_message": "Không thể tạo đơn hàng do lỗi API"
            }
    except Exception as e:
        return {
            "error_type": str(type(e)),
            "error_message": str(e),
            "request_data": quote_data
        }


def handle_case1(params):
    product_info = None
    product_name = params.get("product_name", "")
    user_query = params.get("user_query", "")
    product_main_package = params.get("product_main_package", "")
    product_subpackages = params.get("product_subpackages", "")
    main_package_quantity = params.get("main_package_quantity", "")
    promotion_amount = params.get("promotion_amount", 0)
    promotion_rate = params.get("promotion_rate", 0)
    Company = params.get("Company", "")
    tax_code = params.get("tax_code", "")
    
    # Xử lý product_info như trước
    for product in PRODUCTS:
        if product["AppName"] == product_name:
            product_info = product
            break
    
    if product_info is not None:
        listPackageProduct = []
        for package in product_info["ListPackageProduct"]:
            if "ResourceInfor" in package:
                del package["ResourceInfor"]
            if "ProductID" in package:
                del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info["ListPackageProduct"] = listPackageProduct

    # Sử dụng f-string để thay thế các placeholder
    PROMPT = f"""
Hãy giúp khách hàng tạo đơn hàng dựa theo yêu cầu của họ
Khách hàng muốn mua sản phẩm này {product_name} . Phần trăm chiết khấu {promotion_rate}%, số tiền chiết khấu {promotion_amount}
Đây là thông tin về sản phẩm đó {product_info}
Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {product_main_package} {main_package_quantity}
Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {product_subpackages}
Đây là tin nhắn của khách hàng: {user_query}

# Ý nghĩa các trường thông tin của sản phầm
- "AppCode" : Mã sản phẩm
- "AppName" : Tên sản phẩm
- "ProductID" : ID sản phẩm
- "MarketName" : Tên thị trường của sản phầm đó. Nhận 1 trong 3 giá trị: Hành chính sự nghiệp, Cá nhân, Doanh nghiệp
- "ListPackageProduct" : Danh sách các gói đi kèm sản phẩm đó. Gồm có gói chính, có thể có gói mua thêm và gói dịch vụ đi kèm
    + "ItemPrice": giá tiền của gói
    + "ItemType": Kiểu gói: gói chính, gói mua thêm, gói dịch vụ đi kèm
    + "ItemName" : Tên gói theo cấu hình chính sách giá
    + "ResourceInfo": các thông tin thêm về gói
    + "ModuleName" : Tên nhóm của gói
    + "DisplayName" : Tên của gói, được dùng khi tạo đơn hàng"

Một đơn hàng LUÔN PHẢI được viết ở dạng JSON. Ví dụ đơn hàng mẫu:
{{
    "AppCode" : "CRM",
    "ProductID" : 446,
    "PromotionRate": {promotion_rate},
    "PromotionAmount": {promotion_amount},
    "OrderItemInfos" : [
        {{
            "DisplayName" : "Professional",
            "Quantity" : 3,
            "ModuleName" : "",
        }},
        {{
            "DisplayName" : "Mua thêm 01 người dùng gói Professional",
            "Quantity" : 5,
            "ModuleName" : ""
        }}
    ]
}}

*Lưu ý:
- Nếu thông tin chiết khấu là null thì chuyển thành 0.
- Bạn sẽ cần một chút suy luận để xác giá trị Quantity trong đơn hàng.
- Ví dụ:
Sản phẩm AMIS kế toán có tên gói là Standard năm đầu tiên, khách hàng muốn mua 2 năm, thì Quantity = 2
Sản phẩm AMIS kế toán có tên gói là Mua thêm 01 người dùng gói Professional, khách hàng muốn mua 10 người dùng thì Quantity = 10
Sản phẩm CRM có tên gói Mua thêm 05 người dùng, nhưng người dùng chỉ muốn mua 3 người dùng, thì họ vẫn phải mua 1 gói, như vậy quantity = 1. Nhưng nếu họ muốn mua 7 người dùng, thì họ phải mua 2 gói, như vậy quantity = 2
"""

    USER = f"""
Hãy giúp tôi tạo đơn hàng cho sản phẩm {product_name}
Câu trả lời chỉ là nội dung đơn hàng được viết ở dạng JSON, ngoài ra không chứa thông tin nào khác.
"""

    res = openai_service.structure_response(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": USER},
        ],
        response_format={"type": "text"},
    )
    
    # Xử lý kết quả từ ParsedChatCompletionMessage
    try:
        # Trích xuất nội dung từ đối tượng res
        if hasattr(res, 'content'):
            text = res.content
        else:
            text = str(res)
            
        # Xóa bỏ markdown code block nếu có
        if isinstance(text, str) and text.startswith('```json'):
            text = text[7:]
            if text.endswith('```'):
                text = text[:-3]
        elif isinstance(text, str) and text.startswith('```'):
            text = text[3:]
            if text.endswith('```'):
                text = text[:-3]
        
        # Parse JSON string thành đối tượng Python
        result = json.loads(text)
        
        # Chuyển đổi nếu là dict thành list để xử lý đồng nhất
        if isinstance(result, dict):
            result = [result]
        
        # Thêm CompanyName và TaxCode nếu có
        if Company:
            for item in result:
                item["CompanyName"] = Company
        if tax_code:
            for item in result:
                item["TaxCode"] = tax_code
                
        # Chuyển lại thành chuỗi JSON
        result_json = json.dumps(result, ensure_ascii=False)
        result_json = result_json.replace("\n", " ")
        
        return {
            "result": result_json
        }
    except Exception as e:
        return {
            "error": f"Lỗi xử lý JSON 1: {str(e)}",
            "raw_response": res
        }
def handle_case2(params):
    product_name = params.get("product_name", "")
    product_name_2 = params.get("product_name_2", "")
    user_query = params.get("user_query", "")
    product_main_package = params.get("product_main_package", "")
    product_subpackages = params.get("product_subpackages", "")
    main_package_quantity = params.get("main_package_quantity", "")
    product_main_package_2 = params.get("product_main_package_2", "")
    product_subpackages_2 = params.get("product_subpackages_2", "")
    main_package_quantity_2 = params.get("main_package_quantity_2", "")
    promotion_amount = params.get("promotion_amount", 0)
    promotion_amount_2 = params.get("promotion_amount_2", 0)
    promotion_rate = params.get("promotion_rate", 0)
    promotion_rate_2 = params.get("promotion_rate_2", 0)
    Company = params.get("Company", "")
    tax_code = params.get("tax_code", "")
    
    # Xử lý thông tin cho sản phẩm 1
    product_info = None
    for product in PRODUCTS:
        if product["AppName"] == product_name:
            product_info = product
            break
    if product_info is not None:
        listPackageProduct = []
        for package in product_info["ListPackageProduct"]:
            if "ResourceInfor" in package:
                del package["ResourceInfor"]
            if "ProductID" in package:
                del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info["ListPackageProduct"] = listPackageProduct

    # Xử lý thông tin cho sản phẩm 2
    product_info_2 = None
    for product in PRODUCTS:
        if product["AppName"] == product_name_2:
            product_info_2 = product
            break
    if product_info_2 is not None:
        listPackageProduct = []
        for package in product_info_2["ListPackageProduct"]:
            if "ResourceInfor" in package:
                del package["ResourceInfor"]
            if "ProductID" in package:
                del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info_2["ListPackageProduct"] = listPackageProduct
    
    # Tạo prompt cho OpenAI - sử dụng định dạng mới
    PROMPT = f"""
Hãy giúp người dùng tạo đơn hàng dựa theo yêu cầu của họ
Khách hàng muốn mua các sản phẩm sau
Sản phẩm thứ nhất:
- Tên sản phẩm {product_name} 
- Phần trăm chiết khấu: {promotion_rate}%. Số tiền chiết khấu {promotion_amount}
- Đây là thông tin về sản phẩm đó {product_info}
- Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {product_main_package} {main_package_quantity}
- Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {product_subpackages}
Sản phẩm thứ hai:
- Tên sản phẩm {product_name_2}
- Phần trăm chiết khấu {promotion_rate_2}%. Số tiền chiết khấu {promotion_amount_2}
- Đây là thông tin về sản phẩm đó {product_info_2}
- Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {product_main_package_2}  {main_package_quantity_2}
- Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {product_subpackages_2}
Đây là tin nhắn của người dùng: {user_query}

# Ý nghĩa các trường thông tin của sản phẩm
- "AppCode" : Mã sản phẩm
- "AppName" : Tên sản phẩm
- "ProductID" : ID sản phẩm
- "MarketName" : Tên thị trường của sản phẩm đó. Nhận 1 trong 3 giá trị: Hành chính sự nghiệp, Cá nhân, Doanh nghiệp
- "ListPackageProduct" : Danh sách các gói đi kèm sản phẩm đó. Gồm có gói chính, có thể có gói mua thêm và gói dịch vụ đi kèm
    + "ItemPrice": giá tiền của gói
    + "ItemType": Kiểu gói: gói chính, gói mua thêm, gói dịch vụ đi kèm
    + "ItemName" : Tên gói theo cấu hình chính sách giá
    + "ResourceInfo": các thông tin thêm về gói
    + "ModuleName" : Tên nhóm của gói
    + "DisplayName" : Tên của gói, được dùng khi tạo đơn hàng"

Một đơn hàng LUÔN PHẢI được viết ở dạng JSON. Ví dụ đơn hàng mẫu:
[
    {{
        "AppCode": "CRM",
        "ProductID": 446,
        "PromotionRate": {promotion_rate},
        "PromotionAmount": {promotion_amount},
        "OrderItemInfos": [
            {{
                "DisplayName": "Professional",
                "Quantity": 3,
                "ModuleName": ""
            }},
            {{
                "DisplayName": "Mua thêm 01 người dùng gói Professional",
                "Quantity": 5,
                "ModuleName": ""
            }}
        ]
    }},
    {{
        "AppCode": "Accounting",
        "ProductID": 404,
        "PromotionRate": {promotion_rate_2},
        "PromotionAmount": {promotion_amount_2},
        "OrderItemInfos": [
            {{
                "DisplayName": "Standard",
                "Quantity": 3,
                "ModuleName": ""
            }},
            {{
                "DisplayName": "Mua thêm 01 người dùng gói Standard",
                "Quantity": 5,
                "ModuleName": ""
            }}
        ]
    }}
]

*Lưu ý:
- Nếu thông tin chiết khấu là null thì chuyển thành 0.
- Bạn sẽ cần một chút suy luận để xác định giá trị Quantity trong đơn hàng.
- Ví dụ: 
Sản phẩm AMIS kế toán có tên gói là Standard năm đầu tiên, khách hàng muốn mua 2 năm, thì Quantity = 2
Sản phẩm AMIS kế toán có tên gói là Mua thêm 01 người dùng gói Professional, khách hàng muốn mua 10 người dùng thì Quantity = 10
Sản phẩm CRM có tên gói Mua thêm 05 người dùng, nhưng người dùng chỉ muốn mua 3 người dùng, thì họ vẫn phải mua 1 gói, như vậy quantity = 1. Nhưng nếu họ muốn mua 7 người dùng, thì họ phải mua 2 gói, như vậy quantity = 2
"""

    USER = f"""
    Hãy giúp tôi tạo đơn hàng cho 2 sản phẩm: {product_name} và {product_name_2}.
    Câu trả lời chỉ là nội dung đơn hàng được viết ở dạng JSON, ngoài ra không chứa thông tin nào khác.
"""
    res = openai_service.structure_response(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": USER},
        ],
        response_format={"type": "text"},
    )
    
    # Xử lý kết quả JSON trả về từ OpenAI
    try:
        # Trích xuất nội dung từ đối tượng ParsedChatCompletionMessage
        text = res.content if hasattr(res, 'content') else str(res)
        
        # Xóa bỏ markdown code block nếu có
        if isinstance(text, str) and text.startswith('```json'):
            text = text[7:]
            if text.endswith('```'):
                text = text[:-3]
        elif isinstance(text, str) and text.startswith('```'):
            text = text[3:]
            if text.endswith('```'):
                text = text[:-3]
        
        # Parse JSON string thành đối tượng Python
        result = json.loads(text)
        
        # Chuyển đổi nếu là dict thành list để xử lý đồng nhất
        if isinstance(result, dict):
            result = [result]
        
        # Thêm CompanyName và TaxCode nếu có
        if Company:
            for item in result:
                item["CompanyName"] = Company
        if tax_code:
            for item in result:
                item["TaxCode"] = tax_code
                
        # Chuyển lại thành chuỗi JSON
        result_json = json.dumps(result, ensure_ascii=False)
        result_json = result_json.replace("\n", " ")
        
        return {
            "result": result_json
        }
    except Exception as e:
        return {
            "error": f"Lỗi xử lý JSON 2: {str(e)}",
            "raw_response": res
        }
    
def handle_case3(params):
    product_name = params.get("product_name", "")
    product_name_2 = params.get("product_name_2", "")
    product_name_3 = params.get("product_name_3", "")
    user_query = params.get("user_query", "")
    product_main_package = params.get("product_main_package", "")
    product_subpackages = params.get("product_subpackages", "")
    main_package_quantity = params.get("main_package_quantity", "")
    product_main_package_2 = params.get("product_main_package_2", "")
    product_subpackages_2 = params.get("product_subpackages_2", "")
    main_package_quantity_2 = params.get("main_package_quantity_2", "")
    product_main_package_3 = params.get("product_main_package_3", "")
    product_subpackages_3 = params.get("product_subpackages_3", "")
    main_package_quantity_3 = params.get("main_package_quantity_3", "")
    promotion_amount = params.get("promotion_amount", 0)
    promotion_amount_2 = params.get("promotion_amount_2", 0)
    promotion_amount_3 = params.get("promotion_amount_3", 0)
    promotion_rate = params.get("promotion_rate", 0)
    promotion_rate_2 = params.get("promotion_rate_2", 0)
    promotion_rate_3 = params.get("promotion_rate_3", 0)
    Company = params.get("Company", "")
    tax_code = params.get("tax_code", "")
    
    # Xử lý thông tin cho sản phẩm 1
    product_info = None
    for product in PRODUCTS:
        if product["AppName"] == product_name:
            product_info = product
            break
    if product_info is not None:
        listPackageProduct = []
        for package in product_info["ListPackageProduct"]:
            if "ResourceInfor" in package:
                del package["ResourceInfor"]
            if "ProductID" in package:
                del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info["ListPackageProduct"] = listPackageProduct

    # Xử lý thông tin cho sản phẩm 2
    product_info_2 = None
    for product in PRODUCTS:
        if product["AppName"] == product_name_2:
            product_info_2 = product
            break
    if product_info_2 is not None:
        listPackageProduct = []
        for package in product_info_2["ListPackageProduct"]:
            if "ResourceInfor" in package:
                del package["ResourceInfor"]
            if "ProductID" in package:
                del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info_2["ListPackageProduct"] = listPackageProduct

    # Xử lý thông tin cho sản phẩm 3
    product_info_3 = None
    for product in PRODUCTS:
        if product["AppName"] == product_name_3:
            product_info_3 = product
            break
    if product_info_3 is not None:
        listPackageProduct = []
        for package in product_info_3["ListPackageProduct"]:
            if "ResourceInfor" in package:
                del package["ResourceInfor"]
            if "ProductID" in package:
                del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info_3["ListPackageProduct"] = listPackageProduct
    
    # Prompt 1: Cho sản phẩm 1 và 2
    PROMPT1 = f"""
Hãy giúp người dùng tạo đơn hàng dựa theo yêu cầu của họ
Khách hàng muốn mua các sản phẩm sau
Sản phẩm thứ nhất:
- Tên sản phẩm {product_name} 
- Phần trăm chiết khấu: {promotion_rate}%. Số tiền chiết khấu {promotion_amount}
- Đây là thông tin về sản phẩm đó {product_info}
- Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {product_main_package} {main_package_quantity}
- Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {product_subpackages}
Sản phẩm thứ hai:
- Tên sản phẩm {product_name_2}
- Phần trăm chiết khấu {promotion_rate_2}%. Số tiền chiết khấu {promotion_amount_2}
- Đây là thông tin về sản phẩm đó {product_info_2}
- Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {product_main_package_2} {main_package_quantity_2}
- Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {product_subpackages_2}
Đây là tin nhắn của người dùng: {user_query}

# Ý nghĩa các trường thông tin của sản phẩm
- "AppCode" : Mã sản phẩm
- "AppName" : Tên sản phẩm
- "ProductID" : ID sản phẩm
- "MarketName" : Tên thị trường của sản phẩm đó. Nhận 1 trong 3 giá trị: Hành chính sự nghiệp, Cá nhân, Doanh nghiệp
- "ListPackageProduct" : Danh sách các gói đi kèm sản phẩm đó. Gồm có gói chính, có thể có gói mua thêm và gói dịch vụ đi kèm
    + "ItemPrice": giá tiền của gói
    + "ItemType": Kiểu gói: gói chính, gói mua thêm, gói dịch vụ đi kèm
    + "ItemName" : Tên gói theo cấu hình chính sách giá
    + "ResourceInfo": các thông tin thêm về gói
    + "ModuleName" : Tên nhóm của gói
    + "DisplayName" : Tên của gói, được dùng khi tạo đơn hàng"

Một đơn hàng LUÔN PHẢI được viết ở dạng JSON. Ví dụ đơn hàng mẫu:
[
    {{
        "AppCode": "CRM",
        "ProductID": 446,
        "PromotionRate": {promotion_rate},
        "PromotionAmount": {promotion_amount},
        "OrderItemInfos": [
            {{
                "DisplayName": "Professional",
                "Quantity": 3,
                "ModuleName": ""
            }},
            {{
                "DisplayName": "Mua thêm 01 người dùng gói Professional",
                "Quantity": 5,
                "ModuleName": ""
            }}
        ]
    }},
    {{
        "AppCode": "Accounting",
        "ProductID": 404,
        "PromotionRate": {promotion_rate_2},
        "PromotionAmount": {promotion_amount_2},
        "OrderItemInfos": [
            {{
                "DisplayName": "Standard",
                "Quantity": 3,
                "ModuleName": ""
            }},
            {{
                "DisplayName": "Mua thêm 01 người dùng gói Standard",
                "Quantity": 5,
                "ModuleName": ""
            }}
        ]
    }}
]

*Lưu ý:
- Nếu thông tin chiết khấu là null thì chuyển thành 0.
- Bạn sẽ cần một chút suy luận để xác định giá trị Quantity trong đơn hàng.
- Ví dụ: 
Sản phẩm AMIS kế toán có tên gói là Standard năm đầu tiên, khách hàng muốn mua 2 năm, thì Quantity = 2
Sản phẩm AMIS kế toán có tên gói là Mua thêm 01 người dùng gói Professional, khách hàng muốn mua 10 người dùng thì Quantity = 10
Sản phẩm CRM có tên gói Mua thêm 05 người dùng, nhưng người dùng chỉ muốn mua 3 người dùng, thì họ vẫn phải mua 1 gói, như vậy quantity = 1. Nhưng nếu họ muốn mua 7 người dùng, thì họ phải mua 2 gói, như vậy quantity = 2
"""

    USER1 = f"""
Hãy giúp tôi tạo đơn hàng cho 2 sản phẩm: {product_name} và {product_name_2}.
Câu trả lời chỉ là nội dung đơn hàng được viết ở dạng JSON, ngoài ra không chứa thông tin nào khác.
"""

    # Prompt 2: Cho sản phẩm 3
    PROMPT2 = f"""
Hãy giúp người dùng tạo đơn hàng dựa theo yêu cầu của họ
Khách hàng muốn mua sản phẩm này {product_name_3}
Phần trăm chiết khấu {promotion_rate_3}%. Số tiền chiết khấu {promotion_amount_3}
Đây là thông tin về sản phẩm đó {product_info_3}
Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {product_main_package_3} {main_package_quantity_3}
Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {product_subpackages_3}
Đây là tin nhắn của người dùng: {user_query}

# Ý nghĩa các trường thông tin của sản phẩm
- "AppCode" : Mã sản phẩm
- "AppName" : Tên sản phẩm
- "ProductID" : ID sản phẩm
- "MarketName" : Tên thị trường của sản phẩm đó. Nhận 1 trong 3 giá trị: Hành chính sự nghiệp, Cá nhân, Doanh nghiệp
- "ListPackageProduct" : Danh sách các gói đi kèm sản phẩm đó. Gồm có gói chính, có thể có gói mua thêm và gói dịch vụ đi kèm
    + "ItemPrice": giá tiền của gói
    + "ItemType": Kiểu gói: gói chính, gói mua thêm, gói dịch vụ đi kèm
    + "ItemName" : Tên gói theo cấu hình chính sách giá
    + "ResourceInfo": các thông tin thêm về gói
    + "ModuleName" : Tên nhóm của gói
    + "DisplayName" : Tên của gói, được dùng khi tạo đơn hàng"

Một đơn hàng LUÔN PHẢI được viết ở dạng JSON. Ví dụ đơn hàng mẫu:
{{
    "AppCode" : "CRM",
    "ProductID" : 446,
    "PromotionRate": {promotion_rate_3},
    "PromotionAmount": {promotion_amount_3},
    "OrderItemInfos" : [
        {{
            "DisplayName" : "Professional",
            "Quantity" : 3,
            "ModuleName" : ""
        }},
        {{
            "DisplayName" : "Mua thêm 01 người dùng gói Professional",
            "Quantity" : 5,
            "ModuleName" : ""
        }}
    ]
}}

*Lưu ý:
- Nếu thông tin chiết khấu là null thì chuyển thành 0.
- Bạn sẽ cần một chút suy luận để xác giá trị Quantity trong đơn hàng.
- Ví dụ: 
Sản phẩm AMIS kế toán có tên gói là Standard năm đầu tiên, khách hàng muốn mua 2 năm, thì Quantity = 2
Sản phẩm AMIS kế toán có tên gói là Mua thêm 01 người dùng gói Professional, khách hàng muốn mua 10 người dùng thì Quantity = 10
Sản phẩm CRM có tên gói Mua thêm 05 người dùng, nhưng người dùng chỉ muốn mua 3 người dùng, thì họ vẫn phải mua 1 gói, như vậy quantity = 1. Nhưng nếu họ muốn mua 7 người dùng, thì họ phải mua 2 gói, như vậy quantity = 2
"""

    USER2 = f"""
Hãy giúp tôi tạo đơn hàng cho sản phẩm {product_name_3}
Câu trả lời chỉ là nội dung đơn hàng được viết ở dạng JSON, ngoài ra không chứa thông tin nào khác.
"""

    # Gọi API OpenAI lần 1 cho sản phẩm 1 và 2
    res1 = openai_service.structure_response(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": PROMPT1},
            {"role": "user", "content": USER1},
        ],
        response_format={"type": "text"},
    )
    
    # Gọi API OpenAI lần 2 cho sản phẩm 3
    res2 = openai_service.structure_response(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": PROMPT2},
            {"role": "user", "content": USER2},
        ],
        response_format={"type": "text"},
    )
    
    # Xử lý kết quả JSON trả về từ OpenAI
    try:
        # Xử lý response 1 - Trích xuất nội dung từ đối tượng ParsedChatCompletionMessage
        text1 = res1.content if hasattr(res1, 'content') else str(res1)
        if text1.startswith('```json'):
            text1 = text1[7:-4]
        elif text1.startswith('```'):
            text1 = text1[3:]
            if text1.endswith('```'):
                text1 = text1[:-3]
        
        result1 = json.loads(text1)
        if isinstance(result1, dict):
            result1 = [result1]
            
        # Xử lý response 2
        text2 = res2.content if hasattr(res2, 'content') else str(res2)
        if text2.startswith('```json'):
            text2 = text2[7:-4]
        elif text2.startswith('```'):
            text2 = text2[3:]
            if text2.endswith('```'):
                text2 = text2[:-3]
        
        result2 = json.loads(text2)
        if isinstance(result2, dict):
            result2 = [result2]

        # Kết hợp kết quả từ cả hai lần gọi API
        result1.extend(result2)
        
        # Thêm CompanyName và TaxCode nếu có
        if Company:
            for item in result1:
                item["CompanyName"] = Company
        if tax_code:
            for item in result1:
                item["TaxCode"] = tax_code
                
        # Chuyển lại thành chuỗi JSON
        result = json.dumps(result1, ensure_ascii=False)
        result = result.replace("\n", " ")
        
        return {
            "result": result
        }
    except Exception as e:
        return {
            "error": f"Lỗi xử lý JSON: {str(e)}",
            "raw_response1": res1,
            "raw_response2": res2
        }
def handle_case4(params):
    product_name = params.get("product_name", "")
    product_name_2 = params.get("product_name_2", "")
    product_name_3 = params.get("product_name_3", "")
    product_name_4 = params.get("product_name_4", "")
    user_query = params.get("user_query", "")
    product_main_package = params.get("product_main_package", "")
    product_subpackages = params.get("product_subpackages", "")
    main_package_quantity = params.get("main_package_quantity", "")
    product_main_package_2 = params.get("product_main_package_2", "")
    product_subpackages_2 = params.get("product_subpackages_2", "")
    main_package_quantity_2 = params.get("main_package_quantity_2", "")
    product_main_package_3 = params.get("product_main_package_3", "")
    product_subpackages_3 = params.get("product_subpackages_3", "")
    main_package_quantity_3 = params.get("main_package_quantity_3", "")
    product_main_package_4 = params.get("product_main_package_4", "")
    product_subpackages_4 = params.get("product_subpackages_4", "")
    main_package_quantity_4 = params.get("main_package_quantity_4", "")
    promotion_amount = params.get("promotion_amount", 0)
    promotion_amount_2 = params.get("promotion_amount_2", 0)
    promotion_amount_3 = params.get("promotion_amount_3", 0)
    promotion_amount_4 = params.get("promotion_amount_4", 0)
    promotion_rate = params.get("promotion_rate", 0)
    promotion_rate_2 = params.get("promotion_rate_2", 0)
    promotion_rate_3 = params.get("promotion_rate_3", 0)
    promotion_rate_4 = params.get("promotion_rate_4", 0)
    Company = params.get("Company", "")
    tax_code = params.get("tax_code", "")
    
    # Xử lý thông tin cho sản phẩm 1
    product_info = None
    for product in PRODUCTS:
        if product["AppName"] == product_name:
            product_info = product
            break
    if product_info is not None:
        listPackageProduct = []
        for package in product_info["ListPackageProduct"]:
            if "ResourceInfor" in package:
                del package["ResourceInfor"]
            if "ProductID" in package:
                del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info["ListPackageProduct"] = listPackageProduct

    # Xử lý thông tin cho sản phẩm 2
    product_info_2 = None
    for product in PRODUCTS:
        if product["AppName"] == product_name_2:
            product_info_2 = product
            break
    if product_info_2 is not None:
        listPackageProduct = []
        for package in product_info_2["ListPackageProduct"]:
            if "ResourceInfor" in package:
                del package["ResourceInfor"]
            if "ProductID" in package:
                del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info_2["ListPackageProduct"] = listPackageProduct

    # Xử lý thông tin cho sản phẩm 3
    product_info_3 = None
    for product in PRODUCTS:
        if product["AppName"] == product_name_3:
            product_info_3 = product
            break
    if product_info_3 is not None:
        listPackageProduct = []
        for package in product_info_3["ListPackageProduct"]:
            if "ResourceInfor" in package:
                del package["ResourceInfor"]
            if "ProductID" in package:
                del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info_3["ListPackageProduct"] = listPackageProduct

    # Xử lý thông tin cho sản phẩm 4
    product_info_4 = None
    for product in PRODUCTS:
        if product["AppName"] == product_name_4:
            product_info_4 = product
            break
    if product_info_4 is not None:
        listPackageProduct = []
        for package in product_info_4["ListPackageProduct"]:
            if "ResourceInfor" in package:
                del package["ResourceInfor"]
            if "ProductID" in package:
                del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info_4["ListPackageProduct"] = listPackageProduct
    
    # Prompt 1: Cho sản phẩm 1 và 2
    PROMPT1 = f"""
Hãy giúp người dùng tạo đơn hàng dựa theo yêu cầu của họ
Khách hàng muốn mua các sản phẩm sau
Sản phẩm thứ nhất:
- Tên sản phẩm {product_name} 
- Phần trăm chiết khấu: {promotion_rate}%. Số tiền chiết khấu {promotion_amount}
- Đây là thông tin về sản phẩm đó {product_info}
- Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {product_main_package} {main_package_quantity}
- Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {product_subpackages}
Sản phẩm thứ hai:
- Tên sản phẩm {product_name_2}
- Phần trăm chiết khấu {promotion_rate_2}%. Số tiền chiết khấu {promotion_amount_2}
- Đây là thông tin về sản phẩm đó {product_info_2}
- Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {product_main_package_2} {main_package_quantity_2}
- Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {product_subpackages_2}
Đây là tin nhắn của người dùng: {user_query}

# Ý nghĩa các trường thông tin của sản phẩm
- "AppCode" : Mã sản phẩm
- "AppName" : Tên sản phẩm
- "ProductID" : ID sản phẩm
- "MarketName" : Tên thị trường của sản phẩm đó. Nhận 1 trong 3 giá trị: Hành chính sự nghiệp, Cá nhân, Doanh nghiệp
- "ListPackageProduct" : Danh sách các gói đi kèm sản phẩm đó. Gồm có gói chính, có thể có gói mua thêm và gói dịch vụ đi kèm
    + "ItemPrice": giá tiền của gói
    + "ItemType": Kiểu gói: gói chính, gói mua thêm, gói dịch vụ đi kèm
    + "ItemName" : Tên gói theo cấu hình chính sách giá
    + "ResourceInfo": các thông tin thêm về gói
    + "ModuleName" : Tên nhóm của gói
    + "DisplayName" : Tên của gói, được dùng khi tạo đơn hàng"

Một đơn hàng LUÔN PHẢI được viết ở dạng JSON. Ví dụ đơn hàng mẫu:
[
    {{
        "AppCode": "CRM",
        "ProductID": 446,
        "PromotionRate": {promotion_rate},
        "PromotionAmount": {promotion_amount},
        "OrderItemInfos": [
            {{
                "DisplayName": "Professional",
                "Quantity": 3,
                "ModuleName": ""
            }},
            {{
                "DisplayName": "Mua thêm 01 người dùng gói Professional",
                "Quantity": 5,
                "ModuleName": ""
            }}
        ]
    }},
    {{
        "AppCode": "Accounting",
        "ProductID": 404,
        "PromotionRate": {promotion_rate_2},
        "PromotionAmount": {promotion_amount_2},
        "OrderItemInfos": [
            {{
                "DisplayName": "Standard",
                "Quantity": 3,
                "ModuleName": ""
            }},
            {{
                "DisplayName": "Mua thêm 01 người dùng gói Standard",
                "Quantity": 5,
                "ModuleName": ""
            }}
        ]
    }}
]

*Lưu ý:
- Nếu thông tin chiết khấu là null thì chuyển thành 0.
- Bạn sẽ cần một chút suy luận để xác định giá trị Quantity trong đơn hàng.
- Ví dụ: 
Sản phẩm AMIS kế toán có tên gói là Standard năm đầu tiên, khách hàng muốn mua 2 năm, thì Quantity = 2
Sản phẩm AMIS kế toán có tên gói là Mua thêm 01 người dùng gói Professional, khách hàng muốn mua 10 người dùng thì Quantity = 10
Sản phẩm CRM có tên gói Mua thêm 05 người dùng, nhưng người dùng chỉ muốn mua 3 người dùng, thì họ vẫn phải mua 1 gói, như vậy quantity = 1. Nhưng nếu họ muốn mua 7 người dùng, thì họ phải mua 2 gói, như vậy quantity = 2
"""

    USER1 = f"""
Hãy giúp tôi tạo đơn hàng cho 2 sản phẩm: {product_name} và {product_name_2}.
Câu trả lời chỉ là nội dung đơn hàng được viết ở dạng JSON, ngoài ra không chứa thông tin nào khác.
"""

    # Prompt 2: Cho sản phẩm 3 và 4
    PROMPT2 = f"""
Hãy giúp người dùng tạo đơn hàng dựa theo yêu cầu của họ
Khách hàng muốn mua các sản phẩm sau
Sản phẩm thứ nhất:
- Tên sản phẩm {product_name_3}
- Phần trăm chiết khấu {promotion_rate_3}%. Số tiền chiết khấu {promotion_amount_3}
- Đây là thông tin về sản phẩm đó {product_info_3}
- Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {product_main_package_3} {main_package_quantity_3}
- Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {product_subpackages_3}
Sản phẩm thứ hai:
- Tên sản phẩm {product_name_4}
- Phần trăm chiết khấu {promotion_rate_4}%. Số tiền chiết khấu {promotion_amount_4}
- Đây là thông tin về sản phẩm đó {product_info_4}
- Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {product_main_package_4} {main_package_quantity_4}
- Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {product_subpackages_4}
Đây là tin nhắn của người dùng: {user_query}

# Ý nghĩa các trường thông tin của sản phẩm
- "AppCode" : Mã sản phẩm
- "AppName" : Tên sản phẩm
- "ProductID" : ID sản phẩm
- "MarketName" : Tên thị trường của sản phẩm đó. Nhận 1 trong 3 giá trị: Hành chính sự nghiệp, Cá nhân, Doanh nghiệp
- "ListPackageProduct" : Danh sách các gói đi kèm sản phẩm đó. Gồm có gói chính, có thể có gói mua thêm và gói dịch vụ đi kèm
    + "ItemPrice": giá tiền của gói
    + "ItemType": Kiểu gói: gói chính, gói mua thêm, gói dịch vụ đi kèm
    + "ItemName" : Tên gói theo cấu hình chính sách giá
    + "ResourceInfo": các thông tin thêm về gói
    + "ModuleName" : Tên nhóm của gói
    + "DisplayName" : Tên của gói, được dùng khi tạo đơn hàng"

Một đơn hàng LUÔN PHẢI được viết ở dạng JSON. Ví dụ đơn hàng mẫu:
[
    {{
        "AppCode": "CRM",
        "ProductID": 446,
        "PromotionRate": {promotion_rate_3},
        "PromotionAmount": {promotion_amount_3},
        "OrderItemInfos": [
            {{
                "DisplayName": "Professional",
                "Quantity": 3,
                "ModuleName": ""
            }},
            {{
                "DisplayName": "Mua thêm 01 người dùng gói Professional",
                "Quantity": 5,
                "ModuleName": ""
            }}
        ]
    }},
    {{
        "AppCode": "Accounting",
        "ProductID": 404,
        "PromotionRate": {promotion_rate_4},
        "PromotionAmount": {promotion_amount_4},
        "OrderItemInfos": [
            {{
                "DisplayName": "Standard",
                "Quantity": 3,
                "ModuleName": ""
            }},
            {{
                "DisplayName": "Mua thêm 01 người dùng gói Standard",
                "Quantity": 5,
                "ModuleName": ""
            }}
        ]
    }}
]

*Lưu ý:
- Nếu thông tin chiết khấu là null thì chuyển thành 0.
- Bạn sẽ cần một chút suy luận để xác định giá trị Quantity trong đơn hàng.
- Ví dụ: 
Sản phẩm AMIS kế toán có tên gói là Standard năm đầu tiên, khách hàng muốn mua 2 năm, thì Quantity = 2
Sản phẩm AMIS kế toán có tên gói là Mua thêm 01 người dùng gói Professional, khách hàng muốn mua 10 người dùng thì Quantity = 10
Sản phẩm CRM có tên gói Mua thêm 05 người dùng, nhưng người dùng chỉ muốn mua 3 người dùng, thì họ vẫn phải mua 1 gói, như vậy quantity = 1. Nhưng nếu họ muốn mua 7 người dùng, thì họ phải mua 2 gói, như vậy quantity = 2
"""

    USER2 = f"""
Hãy giúp tôi tạo đơn hàng cho 2 sản phẩm: {product_name_3} và {product_name_4}.
Câu trả lời chỉ là nội dung đơn hàng được viết ở dạng JSON, ngoài ra không chứa thông tin nào khác.
"""

    # Gọi API OpenAI lần 1 cho sản phẩm 1 và 2
     # Gọi API OpenAI lần 1 cho sản phẩm 1 và 2
    res1 = openai_service.structure_response(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": PROMPT1},
            {"role": "user", "content": USER1},
        ],
        response_format={"type": "text"},
    )
    
    # Gọi API OpenAI lần 2 cho sản phẩm 3 và 4
    res2 = openai_service.structure_response(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": PROMPT2},
            {"role": "user", "content": USER2},
        ],
        response_format={"type": "text"},
    )
    
    # Xử lý kết quả JSON trả về từ OpenAI
    try:
        # Xử lý response 1
        text1 = res1.content if hasattr(res1, 'content') else str(res1)
        if text1.startswith('```json'):
            text1 = text1[7:-4]
        elif text1.startswith('```'):
            text1 = text1[3:]
            if text1.endswith('```'):
                text1 = text1[:-3]
        
        result1 = json.loads(text1)
        if isinstance(result1, dict):
            result1 = [result1]
            
        # Xử lý response 2
        text2 = res2.content if hasattr(res2, 'content') else str(res2)
        if text2.startswith('```json'):
            text2 = text2[7:-4]
        elif text2.startswith('```'):
            text2 = text2[3:]
            if text2.endswith('```'):
                text2 = text2[:-3]
        
        result2 = json.loads(text2)
        if isinstance(result2, dict):
            result2 = [result2]

        # Kết hợp kết quả từ cả hai lần gọi API
        result1.extend(result2)
        
        # Thêm CompanyName và TaxCode nếu có
        if Company:
            for item in result1:
                item["CompanyName"] = Company
        if tax_code:
            for item in result1:
                item["TaxCode"] = tax_code
                
        # Chuyển lại thành chuỗi JSON
        result = json.dumps(result1, ensure_ascii=False)
        result = result.replace("\n", " ")
        
        return {
            "result": result
        }
    except Exception as e:
        return {
            "error": f"Lỗi xử lý JSON 4: {str(e)}",
            "raw_response1": res1,
            "raw_response2": res2
        }
    

if __name__ == "__main__":
    result= MisaCrmCreateNewQuote.invoke({
    "product_name": "MISA Mimosa Online",
    "user_query": "Tôi muốn mua 2 năm gói chính và 3 gói mua thêm",
    "product_main_package": "Gói chính",
    "product_subpackages": "Gói mua thêm 1; Gói mua thêm 2",
    "main_package_quantity": "2 năm",
    "promotion_amount": 100000,
    "promotion_rate": 10,
    
    "product_name_2": "MISA Bamboo Online",
    "product_main_package_2": "Gói chính",
    "main_package_quantity_2": "3 tháng",
    "product_subpackages_2": "Gói mua thêm 1; Gói mua thêm 2",
    "promotion_amount_2": 200000,
    "promotion_rate_2": 20,
    
    "product_name_3": "MISA SME 2023",
    "product_main_package_3": "Gói chính",
    "main_package_quantity_3": "4 tháng",
    "product_subpackages_3": "Gói mua thêm 1; Gói mua thêm 2",
    "promotion_amount_3": 300000,
    "promotion_rate_3": 30,
    
    "product_name_4": "AMIS Bán hàng",
    "product_main_package_4": "Gói chính",
    "main_package_quantity_4": "5 tháng",
    "product_subpackages_4": "Gói mua thêm 1; Gói mua thêm 2",
    "promotion_amount_4": 400000,
    "promotion_rate_4": 40,
    
    "Company": "Công ty ABC",
    "tax_code": "1234567890"
    })
    print(result)