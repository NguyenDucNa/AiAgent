from product_info import ProductType, PRODUCTS, MEI_ENTERPRISE_PKG, MEI_HOUSEHOLD_PKG, RESPONSE_CREATE_EXTEND_QUOTE
from pydantic import Field, BaseModel
from langchain_core.tools import tool
from enum import Enum
import os
import sys


# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../../../../.."))
sys.path.append(project_root)

from example.ava_example.src.tools.utils import openai_service

class Input(BaseModel):
    product_name: ProductType = Field(..., description="Tên sản phẩm")
    user_query: str = Field(..., description="Tin nhắn của người dùng")
    product_main_package: str = Field(...,
                                      description="Tên gói chính của sản phẩm")
    product_subpackages: str = Field(
        ..., description="Danh sách các gói mua thêm, gói dịch vụ của sản phẩm thứ nhất, và số lượng tương ứng của mỗi gói")
    main_package_quantity: str = Field(
        ..., description="Số lượng gói chính, có thể tính bằng năm, tháng, gói, khóa học. VD: 2 năm, 3 gói, 1 khóa, ...")
    product_name_2: ProductType = Field(
        ..., description="Tên sản phẩm thứ 2, nếu người dùng muốn mua 2 sản phẩm")
    product_main_package_2: str = Field(...,
                                        description="  Gói chính của sản phẩm thứ 2.")
    main_package_quantity_2: str = Field(
        ..., description="Số lượng gói chính của sản phẩm thứ 2, có thể tính bằng năm, tháng, gói, khóa học. VD: 2 năm, 3 gói, 1 khóa, ...")
    product_subpackages_2: str = Field(
        ..., description="Danh sách các gói mua thêm, gói dịch vụ của sản phẩm thứ 2, và số lượng tương ứng của mỗi gói")
    product_name_3: ProductType = Field(
        ..., description="Tên sản phẩm thứ 3, nếu người dùng muốn mua 3 sản phẩm")
    product_main_package_3: str = Field(...,
                                        description="Gói chính của sản phẩm thứ 3.")
    main_package_quantity_3: str = Field(
        ..., description="Số lượng gói chính của sản phẩm thứ 3, có thể tính bằng năm, tháng, gói, khóa học. VD: 2 năm, 3 gói, 1 khóa, ...")
    product_subpackages_3: str = Field(
        ..., description="Danh sách các gói mua thêm, gói dịch vụ của sản phẩm thứ 3, và số lượng tương ứng của mỗi gói")
    product_name_4: ProductType = Field(
        ..., description="Tên sản phẩm thứ 4, nếu người dùng muốn mua 4 sản phẩm")
    product_main_package_4: str = Field(...,
                                        description="Gói chính của sản phẩm thứ 4.")
    main_package_quantity_4: str = Field(
        ..., description="Số lượng gói chính của sản phẩm thứ 4, có thể tính bằng năm, tháng, gói, khóa học. VD: 2 năm, 3 gói, 1 khóa, ...")
    product_subpackages_4: str = Field(
        ..., description="Danh sách các gói mua thêm, gói dịch vụ của sản phẩm thứ 4, và số lượng tương ứng của mỗi gói")
    promotion_amount: int = Field(
        ..., description="Số tiền chiết khấu của sản phẩm chính. Nếu user không cung cấp thì nhận giá trị 0")
    promotion_amount_2: int = Field(
        ..., description="Số tiền chiết khấu của sản phẩm thứ 2. Nếu user không cung cấp thì nhận giá trị 0")
    promotion_amount_3: int = Field(
        ..., description="Số tiền chiết khấu của sản phẩm thứ 3. Nếu user không cung cấp thì nhận giá trị 0")
    promotion_amount_4: int = Field(
        ..., description="Số tiền chiết khấu của sản phẩm thứ tư. Nếu user không cung cấp thì nhận giá trị 0")
    promotion_rate: int = Field(
        ..., description="Phần trăm (%) chiết khấu của sản phẩm chính. Ví dụ chiết khấu 5% thì nhận giá trị 5. Nếu user không cung cấp thì nhận giá trị 0. ")
    promotion_rate_2: int = Field(
        ..., description="Phần trăm (%) chiết khấu của sản phẩm thứ 2. Ví dụ chiết khấu 5% thì nhận giá trị 5. Nếu user không cung cấp thì nhận giá trị 0. ")
    promotion_rate_3: int = Field(
        ..., description="Phần trăm (%) chiết khấu của sản phẩm thứ 3. Ví dụ chiết khấu 5% thì nhận giá trị 5. Nếu user không cung cấp thì nhận giá trị 0. ")
    promotion_rate_4: int = Field(
        ..., description="Phần trăm (%) chiết khấu của sản phẩm thứ 4. Ví dụ chiết khấu 5% thì nhận giá trị 5. Nếu user không cung cấp thì nhận giá trị 0. ")
    Company: str = Field(..., description="Công ty khách hàng")
    tax_code: str = Field(..., description="Mã số thuế (MST) của khách hàng")


@tool("MisaCrmCreateNewQuote", args_schema=Input, return_direct=False)
def MisaCrmCreateNewQuote(
    product_name: ProductType,
    user_query: str,
    product_main_package: str,
    product_subpackages: str,
    main_package_quantity: str,
    product_name_2: ProductType,
    product_main_package_2: str,
    main_package_quantity_2: str,
    product_subpackages_2: str,
    product_name_3: ProductType,
    product_main_package_3: str,
    main_package_quantity_3: str,
    product_subpackages_3: str,
    product_name_4: ProductType,
    product_main_package_4: str,
    main_package_quantity_4: str,
    product_subpackages_4: str,
    promotion_amount: int,
    promotion_amount_2: int,
    promotion_amount_3: int,
    promotion_amount_4: int,
    promotion_rate: int,
    promotion_rate_2: int,
    promotion_rate_3: int,
    promotion_rate_4: int,
    Company: str,
    tax_code: str,
):
    """
    Sử dụng để tạo báo giá mua mới sản phẩm cho khách hàng. Mỗi sản phẩm gồm 1 gói chính, không giới hạn các gói mua thêm và gói dịch vụ đi kèm (subpackages). Các gói mua thêm và gói dịch vụ đi kèm được trích xuất thành danh sách cách nhau bởi dấu ;
    Ví dụ: "Gói 1; Gói 2; Gói 3"
    """
    print(" ====================== MisaCrmCreateNewQuote ===================")
    # Phân loại các trường hợp dựa vào số lượng sản phẩm và gọi hàm tương ứng
    if not product_name_2 or product_name_2 == "":
        # Trường hợp 1: Chỉ có sản phẩm chính, các sản phẩm 2,3,4 trống
        return handle_case1(product_name)

    elif (product_name_2 and product_name_2 != "") and (not product_name_3 or product_name_3 == ""):
        # Trường hợp 2: Có sản phẩm chính và sản phẩm 2, các sản phẩm 3,4 trống
        return handle_case2()

    elif (product_name_2 and product_name_2 != "") and (product_name_3 and product_name_3 != "") and (not product_name_4 or product_name_4 == ""):
        # Trường hợp 3: Có sản phẩm chính, sản phẩm 2 và 3, sản phẩm 4 trống
        return handle_case3()

    else:
        # Trường hợp 4: Có đủ 4 sản phẩm
        return handle_case4()


def handle_case1(
    product_name,
    user_query="",
    product_main_package="",
    product_subpackages="",
    main_package_quantity="",
    promotion_amount=0,
    promotion_rate=0,
    Company="",
    tax_code=""
):
    product_info = None
    for product in PRODUCTS:
        if product["AppName"] == product_name:
            product_info = product
            break
    if product_info is not None:
        listPackageProduct = []
        for package in product_info["ListPackageProduct"]:
            del package["ResourceInfor"]
            del package["ProductID"]
            if package["ItemType"] == 1:
                package["ItemType"] = "Gói chính"
            elif package["ItemType"] == 2:
                package["ItemType"] = "Gói mua thêm"
            elif package["ItemType"] == 3:
                package["ItemType"] = "Gói dịch vụ đi kèm"
            listPackageProduct.append(package)
        product_info["ListPackageProduct"] = listPackageProduct

    PROMPT = """
Hãy giúp khách hàng tạo đơn hàng dựa theo yêu cầu của họ
Khách hàng muốn mua sản phẩm này {{#1727256321646.product_name#}} . Phần trăm chiết khấu {{#1727256321646.promotion_rate#}}%, số tiền chiết khấu {{#1727256321646.promotion_amount#}}
Đây là thông tin về sản phẩm đó {{#1727321377567.product_info#}} 
Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {{#1727256321646.product_main_package#}}  {{#1727256321646.main_package_quantity#}}
Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {{#1727256321646.product_subpackages#}}
Đây là tin nhắn của khách hàng: {{#1727256321646.user_query#}}

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
{
    "AppCode" : "CRM",
    "ProductID" : 446,
    "PromotionRate": {{#1727256321646.promotion_rate#}},
    "PromotionAmount": {{#1727256321646.promotion_amount#}},
    "OrderItemInfos" : [
        {
            "DisplayName" : "Professional",
            "Quantity" : 3,
            "ModuleName" : "",
        },
        {
            "DisplayName" : "Mua thêm 01 người dùng gói Professional",
            "Quantity" : 5,
            "ModuleName" : ""
        }
    ]
}

*Lưu ý:
- Nếu thông tin chiết khấu là null thì chuyển thành 0.
- Bạn sẽ cần một chút suy luận để xác giá trị Quantity trong đơn hàng.
- Ví dụ: 
Sản phẩm AMIS kế toán có tên gói là Standard năm đầu tiên, khách hàng muốn mua 2 năm, thì Quantity = 2
Sản phẩm AMIS kế toán có tên gói là Mua thêm 01 người dùng gói Professional, khách hàng muốn mua 10 người dùng thì Quantity = 10
Sản phẩm CRM có tên gói Mua thêm 05 người dùng, nhưng người dùng chỉ muốn mua 3 người dùng, thì họ vẫn phải mua 1 gói, như vậy quantity = 1. Nhưng nếu họ muốn mua 7 người dùng, thì họ phải mua 2 gói, như vậy quantity = 2
"""
    USER = """
Hãy giúp tôi tạo đơn hàng cho sản phẩm {{#1727256321646.product_name#}}
Câu trả lời chỉ là nội dung đơn hàng được viết ở dạng JSON, ngoài ra không chứa thông tin nào khác. 
"""

    res = openai_service.structure_response(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": USER},
        ],
        # response_format=ClassificationResponse,
    )
    return {
        "product_info": str(product_info),
    }


def handle_case2():
    print("Xử lý trường hợp 2: Có sản phẩm chính và sản phẩm 2")
    # Các logic xử lý trường hợp 2 sẽ được thêm vào đây
    return {
        "case": 2,
        "message": "Đã xử lý trường hợp có sản phẩm chính và sản phẩm 2"
    }

# Hàm xử lý cho trường hợp 3: Có sản phẩm chính, sản phẩm 2 và 3


def handle_case3():
    print("Xử lý trường hợp 3: Có sản phẩm chính, sản phẩm 2 và 3")
    # Các logic xử lý trường hợp 3 sẽ được thêm vào đây
    return {
        "case": 3,
        "message": "Đã xử lý trường hợp có sản phẩm chính, sản phẩm 2 và 3"
    }

# Hàm xử lý cho trường hợp 4: Có đủ 4 sản phẩm


def handle_case4():
    print("Xử lý trường hợp 4: Có đủ 4 sản phẩm")
    # Các logic xử lý trường hợp 4 sẽ được thêm vào đây
    return {
        "case": 4,
        "message": "Đã xử lý trường hợp có đủ 4 sản phẩm"
    }


PROMPT = """
   Hãy giúp khách hàng tạo đơn hàng dựa theo yêu cầu của họ
Khách hàng muốn mua sản phẩm này {{}} . Phần trăm chiết khấu {{#1727256321646.promotion_rate#}}%, số tiền chiết khấu {{#1727256321646.promotion_amount#}}
Đây là thông tin về sản phẩm đó {{#1727321377567.product_info#}} 
Đây là gói chính của sản phẩm và số lượng mà khách hàng đã chọn {{#1727256321646.product_main_package#}}  {{#1727256321646.main_package_quantity#}}
Đây là các gói mua thêm, gói dịch vụ đi kèm sản phẩm khách hàng đã chọn {{#1727256321646.product_subpackages#}}
Đây là tin nhắn của khách hàng: {{#1727256321646.user_query#}}

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
{
    "AppCode" : "CRM",
    "ProductID" : 446,
    "PromotionRate": {{#1727256321646.promotion_rate#}},
    "PromotionAmount": {{#1727256321646.promotion_amount#}},
    "OrderItemInfos" : [
        {
            "DisplayName" : "Professional",
            "Quantity" : 3,
            "ModuleName" : "",
        },
        {
            "DisplayName" : "Mua thêm 01 người dùng gói Professional",
            "Quantity" : 5,
            "ModuleName" : ""
        }
    ]
}

*Lưu ý:
- Nếu thông tin chiết khấu là null thì chuyển thành 0.
- Bạn sẽ cần một chút suy luận để xác giá trị Quantity trong đơn hàng.
- Ví dụ: 
Sản phẩm AMIS kế toán có tên gói là Standard năm đầu tiên, khách hàng muốn mua 2 năm, thì Quantity = 2
Sản phẩm AMIS kế toán có tên gói là Mua thêm 01 người dùng gói Professional, khách hàng muốn mua 10 người dùng thì Quantity = 10
Sản phẩm CRM có tên gói Mua thêm 05 người dùng, nhưng người dùng chỉ muốn mua 3 người dùng, thì họ vẫn phải mua 1 gói, như vậy quantity = 1. Nhưng nếu họ muốn mua 7 người dùng, thì họ phải mua 2 gói, như vậy quantily = 2
"""


if __name__ == "__main__":
    result= MisaCrmCreateNewQuote.invoke(
        product_name="AMIS CRM",
        user_query="Tôi muốn mua 2 năm gói chính và 3 gói mua thêm",
        product_main_package="Gói chính",
        product_subpackages="Gói mua thêm 1; Gói mua thêm 2",
        main_package_quantity="2 năm",
        # product_name_2="AMIS CRM",
        product_main_package_2="Gói chính",
        main_package_quantity_2="3 tháng",
        product_subpackages_2="Gói mua thêm 1; Gói mua thêm 2",
        # product_name_3="AMIS CRM",
        product_main_package_3="Gói chính",
        main_package_quantity_3="4 tháng",
        product_subpackages_3="Gói mua thêm 1; Gói mua thêm 2",
        # product_name_4="AMIS CRM",
        product_main_package_4="Gói chính",
        main_package_quantity_4="5 tháng",
        product_subpackages_4="Gói mua thêm 1; Gói mua thêm 2",
        promotion_amount=100000,
        promotion_amount_2=200000,
        promotion_amount_3=300000,
        promotion_amount_4=400000,
        promotion_rate=10,
        promotion_rate_2=20,
        promotion_rate_3=30,
        promotion_rate_4=40,
        Company="Công ty ABC",
        tax_code="1234567890"
    )
    print(result)