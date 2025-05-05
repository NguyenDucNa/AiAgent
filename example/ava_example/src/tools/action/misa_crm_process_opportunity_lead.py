import requests
import json
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from enum import Enum

class ActionType(Enum):
    A = "Chuyển đổi tiềm năng"
    B = "Nhận xử lý ao cơ hội"
    C = "Xem chi tiết tiềm năng"
    D = "Xem chi tiết ao cơ hội"
    E = "Tra cứu thông tin liên hệ"
    F = "Xem lịch sử hoạt động"
    G = "Xem lịch sử chăm sóc khách hàng"
    H = "Gợi ý chào bán sản phẩm"
    I = "Xem doanh thu/quy mô nhân sự"
    J = "Xem chi tiết khách hàng"
    K = "Tra cứu sản phẩm đã mua"



class Input(BaseModel):
    action_name: ActionType = Field(..., description="Tên thao tác cần thực hiện",
                             example="Lập báo cáo tài chính")
    tax_code: str = Field(..., description="Mã số thuế của khách hàng",
                          example="0101234567")
    organizationunitid: str = Field(
        ..., description="Mã đơn vị tổ chức của khách hàng", example="123456789")


@tool("MisaCrmProcessOpportunityLead", args_schema=Input, return_direct=False)
def MisaCrmProcessOpportunityLead(action_name: ActionType, tax_code: str, organizationunitid: str):
    """
    Thực hiện các thao tác CRM như: Chuyển đổi tiềm năng, Xem chi tiết cơ hội, Tra cứu thông tin, v.v.
    """
    url = "https://testopenapimisajsc.amis.vn/v1/api/ava/taxcode-info"
    headers = {
        "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
        "x-clientId": "AVA",
    }
    params = {
        "taxCode": tax_code,
    } 

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
    except requests.RequestException as e:
        return {
            "function_calling": {},
            "message": f"Không thể gửi yêu cầu tới API. Chi tiết: {str(e)}"
        }

    if response.status_code != 200:
        return {
            "function_calling": {},
            "message": f"API trả về mã lỗi {response.status_code}."
        }

    try:
        body = response.text
    except Exception as e:
        return {
            "function_calling": {},
            "message": f"Lỗi khi đọc phản hồi API: {str(e)}"
        }

    # Tìm handler phù hợp
    for key, handler in ACTION_HANDLERS.items():
        if key == action_name.value:
            return handler(body, action_name.value)

    # Nếu không tìm được handler phù hợp
    return {
        "function_calling": {},
        "message": f"Không có hàm xử lý cho action_name: {action_name.value}."
    }


# --- Logic xử lý riêng cho từng action ---
def handle_convert_lead(body: str, action_name: str) -> dict:
    if not body:
        return {
            "function_calling": {},
            "message": "Không tìm được dữ liệu"
        }

    data = json.loads(body)
    data_info = data.get("Data", {})
    message = ""
    if data_info:
        first_entry = data_info if isinstance(
            data_info, dict) else data_info[0]
        ID = first_entry.get("ID", "")
        FormLayoutID = first_entry.get("FormLayoutID", 1)

        params = [
            {"name": "LayoutCode", "value": "Lead"},
            {"name": "FormLayoutID", "value": FormLayoutID},
            {"name": "ID", "value": ID},
        ]

        relevant_functions = [
            {"name": "Chuyển đổi tiềm năng", "alias": "Chuyển đổi tiềm năng"},
            {"name": "Xem chi tiết tiềm năng", "alias": "Xem chi tiết tiềm năng"},
        ]

        relevant_functions = [
            func for func in relevant_functions
            if func["name"].lower() != action_name.lower()
        ]

        function_calling = {
            "name": "crm_convert",
            "natural_name": "",
            "params": params,
            "category": "action",
            "relevant_functions": relevant_functions
        }
    else:
        message = "Không tìm được dữ liệu"
        function_calling = {}

    return {
        "function_calling": function_calling,
        "message": message
    }


def handle_opportunity_pool(body: str, action_name: str) -> dict:
    if not body:
        return {
            "function_calling": {},
            "message": "Không tìm được dữ liệu"
        }

    data = json.loads(body)
    data_info = data.get("Data", [])
    message = ""

    if data_info:
        first_entry = data_info if isinstance(
            data_info, dict) else data_info[0]

        ID = first_entry.get("ID", "")
        FormLayoutID = first_entry.get("FormLayoutID", 1)

        params = [
            {"name": "LayoutCode", "value": "OpportunityPool"},
            {"name": "FormLayoutID", "value": FormLayoutID},
            {"name": "ID", "value": ID},
        ]

        function_calling = {
            "name": "crm_convert",
            "natural_name": "",
            "params": params,
            "category": "action",
        }
    else:
        message = "Không tìm được dữ liệu"
        function_calling = {}

    return {
        "function_calling": function_calling,
        "message": message
    }


def handle_view_lead_details(body: str, action_name: str) -> dict:
    if not body:
        return {
            "function_calling": {},
            "message": "Không tìm được dữ liệu"
        }

    data = json.loads(body)
    data_info = data.get("Data", [])
    message = ""

    if data_info:
        first_entry = data_info if isinstance(
            data_info, dict) else data_info[0]

        ID = first_entry.get("ID", "")
        FormLayoutID = first_entry.get("FormLayoutID", 1)

        params = [
            {"name": "LayoutCode", "value": "Lead"},
            {"name": "FormLayoutID", "value": FormLayoutID},
            {"name": "ID", "value": ID},
        ]

        relevant_functions = [
            {"name": "Chuyển đổi tiềm năng", "alias": "Chuyển đổi tiềm năng"},
            {"name": "Xem chi tiết tiềm năng", "alias": "Xem chi tiết tiềm năng"},
        ]

        # Loại bỏ action hiện tại ra khỏi relevant_functions
        relevant_functions = [
            func for func in relevant_functions
            if func["name"].lower() != action_name.lower()
        ]

        function_calling = {
            "name": "crm_view",
            "natural_name": "",
            "params": params,
            "category": "action",
            "relevant_functions": relevant_functions,
        }
    else:
        message = "Không tìm được dữ liệu"
        function_calling = {}

    return {
        "function_calling": function_calling,
        "message": message
    }


def handle_view_opportunity_details(body: str, action_name: str) -> dict:
    """
    Xử lý action "Xem chi tiết cơ hội" trong CRM.
    """
    if not body:
        message = "Không tìm được dữ liệu"
        function_calling = {}
        return {
            "function_calling": function_calling,
            "message": message
        }

    data = json.loads(body)
    data_info = data.get("Data", [])
    message = ""

    if data_info:
        first_entry = data_info if isinstance(
            data_info, dict) else data_info[0]

        # Extract fields from the first entry in Data
        ID = first_entry.get("ID", "")
        FormLayoutID = first_entry.get("FormLayoutID", 1)

        # Define the parameters safely
        params = [
            {"name": "LayoutCode", "value": "Opportunity"},
            {"name": "FormLayoutID", "value": FormLayoutID},
            {"name": "ID", "value": ID}
        ]

        relevant_functions = [
            {'name': 'Xem chi tiết cơ hội', 'alias': 'Xem chi tiết cơ hội'},
            {'name': 'Nhận xử lý cơ hội', 'alias': 'Nhận xử lý cơ hội'}
        ]

        # Filter out the current action from the relevant functions
        relevant_functions = [
            func for func in relevant_functions if func["name"].lower() != action_name.lower()]

        function_calling = {
            "name": "crm_view",
            "natural_name": "",
            "params": params,
            "category": "action",
            "relevant_functions": relevant_functions
        }
    else:
        message = "Không tìm được dữ liệu"
        function_calling = {}

    # Return extracted information
    return {
        "function_calling": function_calling,
        "message": message
    }


def handle_contact_information_lookup(body: str, action_name: str) -> dict:
    """
    Xử lý action "Tra cứu thông tin liên hệ" trong CRM.
    """
    if not body:
        message = "Không tìm được dữ liệu"
        function_calling = {}
        return {
            "function_calling": function_calling,
            "message": message
        }

    data = json.loads(body)
    data_info = data.get("Data", [])
    message = ""

    if data_info:
        first_entry = data_info if isinstance(
            data_info, dict) else data_info[0]

        # Extract fields from the first entry in Data
        ID = first_entry.get("ID", "")
        Module = first_entry.get("Module", 1)
        FormLayoutID = first_entry.get("FormLayoutID", 1)

        # Define the parameters safely
        params = [
            {"name": "LayoutCode", "value": "Account"},
            {"name": "Module", "value": "Contact"},
            {"name": "FormLayoutID", "value": FormLayoutID},
            {"name": "ID", "value": ID}
        ]

        relevant_functions = [
            {"name": "Lịch sử hoạt động", "alias": "Lịch sử hoạt động"},
            {"name": "Lịch sử chăm sóc KH", "alias": "Lịch sử chăm sóc KH"},
            {"name": "Gợi ý chào bán sản phẩm", "alias": "Gợi ý chào bán sản phẩm"},
            {"name": "Tra cứu thông tin liên hệ",
                "alias": "Tra cứu thông tin liên hệ"},
            {"name": "Doanh thu/quy mô nhân sự",
                "alias": "Doanh thu/quy mô nhân sự"},
            {"name": "Thêm cơ hội", "alias": "Thêm cơ hội"}
        ]

        # Lọc các chức năng liên quan để loại bỏ action hiện tại
        relevant_functions = [
            func for func in relevant_functions if func["name"] != action_name]

        # Định nghĩa các thông số cho function call
        function_calling = {
            "name": "crm_lookup",
            "natural_name": "",
            "params": params,
            "category": "action",
            "relevant_functions": relevant_functions
        }
    else:
        message = "Không tìm được dữ liệu"
        function_calling = {}

    # Trả về thông tin đã xử lý
    return {
        "function_calling": function_calling,
        "message": message
    }


def handle_activity_history_lookup(body: str, action_name: str) -> dict:
    """
    Xử lý action "Lịch sử hoạt động" trong CRM.
    Trả về ID từ dữ liệu và các thông tin liên quan.
    """
    if not body:
        return {
            "function_calling": {
                "name": "",
                "natural_name": "",
                "params": [],
                "category": "action"
            },
            "instruction": "Không tìm thấy thông tin",
            "HistoryDeals": [{}]
        }

    data = json.loads(body)
    data_info = data.get("Data", {})
    message = "Dữ liệu bao gồm Mã phân hệ, Tiêu đề, Mô tả, Người tạo, Số thứ tự, Ngày tạo. Hãy dựa vào dữ liệu để trả về thông tin tóm tắt lịch sử hoạt động của khách hàng."
    answer_format = """Gợi ý chào bán sản phẩm: 
    - Sản phẩm <Tên sản phẩm>, thông tin liên hệ <Thông tin liên hệ>"""

    if data_info:
        if isinstance(data_info, dict):
            data_info = data_info.get("HistoryDeals")
    else:
        message = "Không tìm được dữ liệu"
        data_info = [{}]

    # API bổ sung để lấy lịch sử hoạt động
    activity_history = []
    try:
        api_url = "https://testopenapimisajsc.amis.vn/v1/api/ava/account/history/account/"
        headers = {
            "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
            "x-clientId": "AVA",
        }
        response = requests.get(f"{api_url}{id}", headers=headers, timeout=10)
        response.raise_for_status()  # Kiểm tra mã trạng thái HTTP

        # Parse dữ liệu từ API bổ sung
        activity_data = response.json()
        activity_history = activity_data.get("ActivityHistory", [])
    except requests.exceptions.RequestException as e:
        activity_history = []
        message = f"Lỗi khi gọi API bổ sung: {str(e)}"

    # Relevant functions mà bạn muốn trừ đi action hiện tại
    relevant_functions = [
        {"name": "Lịch sử hoạt động", "alias": "Lịch sử hoạt động"},
        {"name": "Lịch sử chăm sóc KH", "alias": "Lịch sử chăm sóc KH"},
        {"name": "Gợi ý chào bán sản phẩm", "alias": "Gợi ý chào bán sản phẩm"},
        {"name": "Tra cứu thông tin liên hệ", "alias": "Tra cứu thông tin liên hệ"}
    ]
    relevant_functions = [
        func for func in relevant_functions if func["name"] != action_name]

    # Chuẩn bị gọi function
    function_calling = {
        "name": "crm_history",
        "natural_name": "",
        "params": [
            {
                "name": "ID",
                "value": id
            },
            {
                "name": "LayoutCode",
                "value": "Account"
            }
        ],
        "category": "action",
        "relevant_functions": relevant_functions
    }

    return {
        "function_calling": function_calling,
        "instruction": message,
        "HistoryDeals": data_info,
        "ActivityHistory": activity_history
    }


def handle_customer_care_history_lookup(body: str, action_name: str) -> dict:
    """
    Xử lý action "Lịch sử chăm sóc KH" trong CRM.
    Trả về thông tin liên quan đến khách hàng và các chức năng có sẵn.
    """
    if not body:
        message = "Không tìm được dữ liệu"
        function_calling = {}
        return {
            "function_calling": function_calling,
            "message": message
        }

    data = json.loads(body)

    data_info = data.get("Data", [])
    message = "Không tìm được dữ liệu"
    if data_info:

        first_entry = data_info if isinstance(
            data_info, dict) else data_info[0]

        # Extract fields from the first entry in Data
        ID = first_entry.get("ID", "")
        FormLayoutID = first_entry.get("FormLayoutID", 1)

        # Define the parameters safely
        params = [
            {
                "name": "ID",
                "value": ID
            },
            {
                "name": "FormLayoutID",
                "value": FormLayoutID
            }
        ]

        # Define relevant functions, excluding the current action name
        relevant_functions = [
            {"name": "Lịch sử hoạt động", "alias": "Lịch sử hoạt động"},
            {"name": "Lịch sử chăm sóc KH", "alias": "Lịch sử chăm sóc KH"},
            {"name": "Gợi ý chào bán sản phẩm", "alias": "Gợi ý chào bán sản phẩm"},
            {"name": "Tra cứu thông tin liên hệ",
                "alias": "Tra cứu thông tin liên hệ"}
        ]

        # Filter out the current action name
        relevant_functions = [
            func for func in relevant_functions if func["name"] != action_name]

        # Construct the function call details
        function_calling = {
            "name": "crm_customer_care",
            "natural_name": "",
            "params": params,
            "category": "action",
            "relevant_functions": relevant_functions
        }
    else:
        function_calling = {}

    # Return the extracted information and message
    return {
        "function_calling": function_calling,
        "message": message
    }


def handle_product_sales_suggestion(body: str, action_name: str) -> dict:
    """
    Xử lý hành động "Gợi ý chào bán sản phẩm" trong CRM.
    Trả về thông tin về sản phẩm và người liên hệ cho việc chào bán.
    """
    if not body:
        return {
            "answer_format": "",
            "instruction": "Không tìm thấy thông tin",
            "data": [{}],
            "function_calling": {}
        }

    data = json.loads(body)
    data_info = data.get("Data", [])

    if data_info:
        # Lấy ID từ dữ liệu đầu vào
        first_entry = data_info if isinstance(data_info, dict) else data_info[0]
        ID = first_entry.get("ID", "")
    else:
        ID = ""

    # Gọi API để lấy thông tin sản phẩm
    api_url = f"https://testopenapimisajsc.amis.vn/v1/api/ava/product-info/{ID}/00000000-0000-0000-0000-000000000000"
    headers = {
        "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
        "x-clientId": "AVA",
    }
    
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        status_code = response.status_code
        body = response.text
        
        if status_code == 404:
            return {
                "answer_format": "",
                "instruction": "Không tìm thấy thông tin",
                "data": [{}],
                "function_calling": {}
            }
            
    except requests.exceptions.RequestException as e:
        return {
            "answer_format": "",
            "instruction": f"Lỗi khi gọi API: {str(e)}",
            "data": [{}],
            "function_calling": {}
        }

    if not body:
        return {
            "answer_format": "",
            "instruction": "Không tìm thấy thông tin",
            "data": [{}],
            "function_calling": {}
        }

    data = json.loads(body)
    data_info = data.get("Data", {})

    try:
        for item in data_info:
            # Get all name in Product to a list
            product_names = [product["Name"] for product in item["Product"]]

            # Remove "Product" key in item and add new key "List_product_names" with value is product_names
            item.pop("Product")
            item["List_product_names"] = product_names
            
            # Rename "ContactName" by Contact
            item["Contact"] = item.pop("ContactName")
    except Exception as e:
        print(f"Lỗi khi xử lý dữ liệu sản phẩm: {str(e)}")
        pass

    message = "Dữ liệu bao gồm người liên hệ, danh sách sản phẩm. Hãy dựa vào dữ liệu để trả về thông tin cho người dùng. Hãy trả thông tin dựa theo answer_format. Lưu ý: Hãy trả ra lần lượt các sản phẩm trong danh sách sản phẩm, cuối cùng trả ra y nguyên thông tin liên hệ (Contact) tương ứng với danh sách sản phẩm. Lưu ý: Trường thông tin liên hệ có thể không phải là tên người"
    answer_format = """Gợi ý chào bán sản phẩm: 
    - Danh sách Sản phẩm <Tên sản phẩm>
    Thông tin liên hệ <Contact của danh sách trên>"""
    
    if data_info:
        if isinstance(data_info, dict):
            data_info = [data_info]
    else:
        message = "Không tìm được dữ liệu"
        data_info = [{}]
        function_calling = {}

    relevant_functions = [
        {"name": "Lịch sử hoạt động", "alias": "Lịch sử hoạt động"}, 
        {"name": "Lịch sử chăm sóc KH", "alias": "Lịch sử chăm sóc KH"},
        {"name": "Gợi ý chào bán sản phẩm", "alias": "Gợi ý chào bán sản phẩm"},
        {"name": "Tra cứu thông tin liên hệ", "alias": "Tra cứu thông tin liên hệ"}
    ]

    relevant_functions = [func for func in relevant_functions if func["name"] != action_name]
    function_calling = {
        "natural_name": "",
        "params": [],
        "category": "",
        "relevant_functions": relevant_functions
    }

    # Return extracted information
    return {
        "instruction": message,
        "answer_format": answer_format,
        "data": data_info,
        "function_calling": function_calling
    }

def handle_revenue_view(body: str, action_name: str) -> dict:
    """
    Xử lý hành động "Doanh thu/quy mô nhân sự" trong CRM.
    Trả về thông tin về doanh thu và quy mô nhân sự của công ty.
    """
    if not body:
        return {
            "message": "Không tìm thấy thông tin",
            "data": {},
            "function_calling": {}
        }

    data = json.loads(body)
    data_info = data.get("Data", [])
    message = "Dữ liệu bao gồm doanh thu và quy mô nhân sự. Hãy dựa vào dữ liệu để trả về thông tin cho người dùng"
    
    if data_info:
        first_entry = data_info if isinstance(data_info, dict) else data_info[0]
        ID = first_entry.get("ID", "")
        
        # Gọi API để lấy thông tin chi tiết về doanh thu và nhân sự
        try:
            api_url = "https://testopenapimisajsc.amis.vn/v1/api/ava/account/{ID}"
            headers = {
                "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
                "x-clientId": "AVA",
            }
            
            response = requests.get(api_url, headers=headers, timeout=10)
            if response.status_code == 200:
                revenue_data = response.json()
                # Kết hợp dữ liệu API với dữ liệu hiện có
                if revenue_data.get("Data"):
                    first_entry.update(revenue_data.get("Data"))
            else:
                print(f"API trả về mã lỗi: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi gọi API chi tiết doanh thu: {str(e)}")
    else:
        message = "Không tìm được dữ liệu"
        first_entry = {}
        function_calling = {}
        return {
            "message": message,
            "data": first_entry,
            "function_calling": {}
        }

    relevant_functions = [
        {"name": "Lịch sử hoạt động", "alias": "Lịch sử hoạt động"}, 
        {"name": "Lịch sử chăm sóc KH", "alias": "Lịch sử chăm sóc KH"},
        {"name": "Gợi ý chào bán sản phẩm", "alias": "Gợi ý chào bán sản phẩm"},
        {"name": "Tra cứu thông tin liên hệ", "alias": "Tra cứu thông tin liên hệ"},
        {"name": "Doanh thu/quy mô nhân sự", "alias": "Doanh thu/quy mô nhân sự"},
        {"name": "Thêm cơ hội", "alias": "Thêm cơ hội"}
    ]

    relevant_functions = [func for func in relevant_functions if func["name"] != action_name]

    function_calling = {
        "natural_name": "",
        "params": [],
        "category": "",
        "relevant_functions": relevant_functions
    }
    
    # Return extracted information
    return {
        "message": message,
        "data": first_entry,
        "function_calling": function_calling
    }

def handle_view_customer_details(body: str, action_name: str) -> dict:
    """
    Xử lý hành động "Xem chi tiết khách hàng" trong CRM.
    Trả về thông tin chi tiết của khách hàng nếu có dữ liệu.
    """
    if not body:
        message = "Không tìm được dữ liệu"
        function_calling = {}
        return {
            "function_calling": function_calling,
            "message": message
        }

    data = json.loads(body)

    data_info = data.get("Data", [])
    message = ""
    if data_info:

        first_entry = data_info if isinstance(
            data_info, dict) else data_info[0]

        # Extract fields from the first entry in Data
        ID = first_entry.get("ID", "")
        Module = first_entry.get("Module", 1)
        FormLayoutID = first_entry.get("FormLayoutID", 1)

        # Define the parameters safely
        params = [
            {
                "name": "LayoutCode",
                "value": "Account"
            },
            {
                "name": "FormLayoutID",
                "value": FormLayoutID
            },
            {
                "name": "ID",
                "value": ID
            }
        ]

        # Prepare the function calling details
        function_calling = {
            "name": "crm_lookup",
            "natural_name": "",
            "params": params,
            "category": "action"
        }
    else:
        message = "Không tìm được dữ liệu"
        function_calling = {}

    # Return extracted information
    return {
        "function_calling": function_calling,
        "message": message
    }


def handle_product_lookup(body: str):
    """
    Xử lý dữ liệu JSON để trả về thông tin về các cơ hội sản phẩm của khách hàng.
    """
    res = json.loads(body)
    data = res.get("Data")

    # Hướng dẫn về cách trả lời
    instruction = """
    Dựa trên answer_format để đưa ra câu trả lời.
    """.strip()

    # Định dạng câu trả lời
    answer_format = """
    Format câu trả lời:
    Thông tin Mã số thuế "...":
    - Tên công ty:
    - Địa chỉ:
    - Ngành nghề chính:
    - Tình trạng hoạt động:
    KH <Tên khách hàng trên phân hệ KH> đang tìm hiểu bộ sản phẩm "Tên sản phẩm trên phân hệ KD" từ ngày  <ngày trên KH >, trước đó KH đã tìm hiểu sản phẩm <tên sản phẩm khác trên khách hàng> ngày <ngày sinh cơ hội thất bại>. KH đã mua sản phẩm (Tên đơn hàng)- thêm user - KD chăm sóc
    """.strip()

    if data:
        key_mapping = {
            "Opportunity1": "Opportunity1 - Khách hàng đang tìm hiểu bộ sản phẩm",
            "Opportunity2": "Opportunity2 - Trước đó Khách hàng đã tìm hiểu sản phẩm",
            "Opportunity3": "Opportunity3 - Khách hàng đã mua sản phẩm"
        }

        # Kiểm tra nếu dữ liệu là một danh sách các từ điển
        if isinstance(data, list) and all(isinstance(record, dict) for record in data):
            # Nếu là danh sách các từ điển, tiến hành xử lý từng bản ghi
            for record in data:
                if "Opportunitys" in record:
                    # Áp dụng key mapping cho các cơ hội sản phẩm
                    record["Opportunitys"] = {
                        key_mapping.get(k, k): v for k, v in record["Opportunitys"].items()
                    }
        elif isinstance(data, dict):
            # Nếu dữ liệu là một từ điển duy nhất
            if "Opportunitys" in data:
                # Áp dụng key mapping cho các cơ hội sản phẩm
                data["Opportunitys"] = {
                    key_mapping.get(k, k): v for k, v in data["Opportunitys"].items()
                }

    # Chuẩn bị dữ liệu trả về
    return_data = data[:1] if isinstance(data, list) else [
        data] if isinstance(data, dict) else None

    return {
        "instruction": instruction,
        "data": return_data,
        "answer_format": answer_format
    }


# --- Map action_name đến function xử lý ---
ACTION_HANDLERS = {
    "Chuyển đổi tiềm năng": handle_convert_lead,
    "Nhận xử lý ao cơ hội": handle_opportunity_pool,
    "Xem chi tiết tiềm năng": handle_view_lead_details,
    "Xem chi tiết cơ hội": handle_view_opportunity_details,
    "Tra cứu thông tin liên hệ": handle_contact_information_lookup,
    "Xem lịch sử hoạt động": handle_activity_history_lookup,
    "Xem lịch sử chăm sóc khách hàng": handle_customer_care_history_lookup,
    "Gợi ý chào bán sản phẩm": handle_product_sales_suggestion,
    "Xem doanh thu/quy mô nhân sự": handle_revenue_view,
    "Xem chi tiết khách hàng": handle_view_customer_details,
    "Tra cứu sản phẩm đã mua": handle_product_lookup,
}


if __name__ == "__main__":
    result = MisaCrmProcessOpportunityLead.invoke({
        "action_name": "Xem doanh thu/quy mô nhân sự",
        "tax_code": "0110115204",
        "organizationunitid": "123456789"
    })
    print(result)
