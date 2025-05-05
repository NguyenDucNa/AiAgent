from pydantic import Field, BaseModel
from langchain_core.tools import tool


class Input(BaseModel):
    OrganizationUnitID: str = Field(
        ...,
        description="OrganizationUnitID is from infor_for_view_detail_action"
    )
    ToDate: str = Field(
        ...,
        description="ToDate is from infor_for_view_detail_action"
    )
    FromDate: str = Field(
        ...,
        description="FromDate is from infor_for_view_detail_action"
    )
    IsViewEmployee: str = Field(
        ...,
        description="IsViewEmployee is from infor_for_view_detail_action"
    )
    name_of_fuction_calling: str = Field(
        ...,
        description="name_of_fuction_calling is from infor_for_view_detail_action"
    )
    FromDateBefore: str = Field(
        ...,
        description="FromDateBefore is from infor_for_view_detail_action"
    )
    ToDateBefore: str = Field(
        ...,
        description="ToDateBefore is from infor_for_view_detail_action"
    )


@tool("MisaCrmViewDetailKien", args_schema=Input, return_direct=False)
def MisaCrmViewDetailKien(
    OrganizationUnitID: str,
    ToDate: str,
    FromDate: str,
    IsViewEmployee: str,
    name_of_fuction_calling: str,
    FromDateBefore: str,
    ToDateBefore: str,
):
    """Chỉ sử dụng khi có yêu cầu "Xem chi tiết" , "Xem doanh số chi tiết của đơn vị".
 **luôn thực thi sau khi đã thực thi tool CRM_Revenue_Overview_KIEN**

- Phải lấy lấy giá trị các biến inputs từ  "infor_for_view_detail_action"
- Ưu tiên lấy OrganizationUnitID bằng OrganizationUnitID_Of_Employee.
** Không được hỏi lại người dùng bất cứ điều gì**"""
    print(" ====================== MisaCRMVIewDetailKien ===================")

    # Define the parameters list
    params = [
        {
            "name": "OrganizationUnitID",
            "value": OrganizationUnitID
        },
        {
            "name": "ToDate",
            "value": ToDate
        },
        {
            "name": "FromDate",
            "value": FromDate
        },
        {
            "name": "FromDateBefore",
            "value": FromDateBefore
        },
        {
            "name": "ToDateBefore",
            "value": ToDateBefore
        },
        {   
            "name": "IsViewEmployee",
            "value": IsViewEmployee
        }
    ]

    # Define the function_calling dictionary
    function_calling = {
        "name": name_of_fuction_calling,
        "natural_name": "",
        "params": params,
        "category": "report",
    }

    # Return the result
    return {
        "function_calling": function_calling,
    }

   