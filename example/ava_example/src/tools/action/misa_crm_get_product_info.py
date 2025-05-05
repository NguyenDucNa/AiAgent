from pydantic import Field, BaseModel
from langchain_core.tools import tool
from enum import Enum
import os
import sys

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
sys.path.append(project_root)
from product_info import ProductType, PRODUCTS, MEI_ENTERPRISE_PKG, MEI_HOUSEHOLD_PKG


class Input(BaseModel):
    product_name: ProductType = Field(..., description="The type of product")


@tool("MisaCrmGetProductInfo", args_schema=Input, return_direct=False)
def MisaCrmGetProductInfo(product_name: ProductType):
    """
  Sử dụng để lấy thông tin về sản phẩm. Các thông tin có thể lấy bao gồm: Tên sản phẩm, mã sản phẩm, giá sản phẩm, các gói chính, gói mua thêm, gói dịch vụ đi kèm, ...
    """
    product_info = None
    for product in PRODUCTS:
        if product["AppName"] == product_name.value:
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
    return {
        "product_info": str(product_info),
    }


if __name__ == "__main__":
    result = MisaCrmGetProductInfo.invoke({
        "product_name": "MISA Quản lý tài sản"
    })
    print(result)
