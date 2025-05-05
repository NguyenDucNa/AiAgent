from pydantic import Field, BaseModel
from langchain_core.tools import tool
import re
import requests
import json


class Input(BaseModel):
    MST: str = Field(
        ...,
        description="Mã số thuế của khách hàng"
    )


@tool("MisaCrmSearchMst", args_schema=Input, return_direct=False)
def MisaCrmSearchMst(
    MST: str
):
    """Sử dụng tools này để tìm kiếm thông tin khách hàng theo mã số thuế"""
    print(" ====================== MisaCrmSearchMst ===================")

    # Chuẩn hóa mã số thuế
    tax_code = str(MST).strip().replace(" ", "")

    # Định nghĩa các biểu thức chính quy để kiểm tra mã số thuế
    re_tax_old = re.compile(r"^\d{10}(?:-\d{3}|\d{3})?$")
    re_tax = re.compile(r"^[0-9]{10}$|^[0-9]{13}$|^[0-9]{10}(\s|-)[0-9]{3}$")

    # Kiểm tra mã số thuế với các biểu thức chính quy
    tax = re_tax.match(tax_code)
    tax_old = re_tax_old.match(tax_code)

    if tax and tax_old and (len(tax_code) == 10 or len(tax_code) == 14):        
        # Chuẩn hóa mã số thuế nếu có dấu "-"
        new_tax = tax_code.split('-')[0] if '-' in tax_code else tax_code
        int_arr = [int(x) for x in new_tax]

        # Tính toán kiểm tra tính hợp lệ của mã số thuế
        temp = (int_arr[0] * 31 + int_arr[1] * 29 + int_arr[2] * 23 +
                int_arr[3] * 19 + int_arr[4] * 17 + int_arr[5] * 13 +
                int_arr[6] * 7 + int_arr[7] * 5 + int_arr[8] * 3)

        # Kiểm tra chữ số cuối cùng
        if int_arr[9] == 10 - (temp % 11):
            if len(tax_code) == 14:
                # Kiểm tra mã chi nhánh
                branch_code = tax_code[11:14]
                if branch_code == "000" or branch_code == "-000":
                    return {
                        "result": f"Mã số thuế {MST} không hợp lệ hoặc không tồn tại. Có thể do đang thực hiện thủ tục đăng ký với cơ quan thuế. Vui lòng kiểm tra và cung cấp lại thông tin."
                    }
                else:
                    sub_tax = tax_code[:10]
                    # Gọi API khi mã số thuế hợp lệ
                    return call_api(sub_tax)

            # Gọi API khi mã số thuế hợp lệ
            return call_api(tax_code)

        # Nếu không hợp lệ
        return {
            "result": f"Mã số thuế {MST} không hợp lệ hoặc không tồn tại. Có thể do đang thực hiện thủ tục đăng ký với cơ quan thuế. Vui lòng kiểm tra và cung cấp lại thông tin."
        }

    # Nếu không khớp với biểu thức chính quy
    return {
        "result": f"Mã số thuế {MST} không hợp lệ hoặc không tồn tại. Có thể do đang thực hiện thủ tục đăng ký với cơ quan thuế. Vui lòng kiểm tra và cung cấp lại thông tin."
    }


def call_api(tax_code: str) -> dict:
    """Gọi API để tìm kiếm thông tin khách hàng theo mã số thuế"""
    url = "https://testopenapimisajsc.amis.vn/v1/api/ava/taxcode-info"
    headers = {
        "x-clientId": "AVA",
        "x-secretId": "U29tZSByYW5kb20gZGF0YSB0byBlbmNvZGUgaW4gQmFzZTY0Lg==",
        "Content-Type": "application/json",
    }
    params = {
        "taxcode": tax_code
    }

    try:
        # Gửi yêu cầu POST đến API
        response = requests.get(url, headers=headers, params=params)
        status_code = response.status_code
        body = response.text  # Lấy nội dung phản hồi từ API dưới dạng chuỗi JSON

        if status_code == 200:
            res = json.loads(body)
            data = res.get("Data")
            if isinstance(data, dict):
                data = [data]
            # Lấy giá trị flow từ phản hồi, mặc định là 10
            flow = res.get("Type", 10)

            # Gọi hàm handle_flow để xử lý logic tương ứng
            return handle_flow(flow, data, tax_code)
        else:
            return {
                "result": "error",
                "message": f"Lỗi HTTP: {status_code}",
                "flow": 99
            }

    except Exception as e:
        # Xử lý ngoại lệ
        print(f"Error occurred: {e}")
        return {
            "result": "error",
            "message": "Đã xảy ra lỗi trong quá trình gọi API.",
            "flow": 99
        }


def handle_flow(flow: int, data: list, taxCode: str) -> dict:
    """Hàm điều phối xử lý logic dựa trên giá trị của flow"""
    # Từ điển ánh xạ flow đến các hàm xử lý
    dispatcher = {
        2: lambda data: handle_flow_2_or_default(taxCode),
        3: handle_flow_3,
        4: handle_flow_4,
        5: handle_flow_5,
        6: handle_flow_6,
        7: handle_flow_7,
        99: handle_flow_99,
        10: lambda data: handle_flow_2_or_default(taxCode),
    }

    # Lấy hàm xử lý từ dispatcher, nếu không có thì dùng hàm mặc định
    handler = dispatcher.get(
        flow, lambda data: handle_flow_2_or_default(taxCode))

    # Gọi hàm xử lý và trả về kết quả
    return handler(data)


# Hàm xử lý cho flow = 2/10
def handle_flow_2_or_default(taxCode: str) -> dict:
    url = "https://org.misa.vn/org-info/v3/suggest"
    headers = {
        "apikey": "C8h8r7mMqBAFY70C0iY1CJ1n5bZoy4ss",
        "project": "rd-crawler",
        "Content-Type": "application/json"
    }
    params = {
        # la taxcode input dau vao
        "taxcode": taxCode,
    }

    try:
        # Gửi yêu cầu GET đến API
        response = requests.get(url, headers=headers, params=params)
        status_code = response.status_code
        body = response.text  # Lấy nội dung phản hồi từ API dưới dạng chuỗi JSON

        result = [{}]
        check_data = "False"
        if status_code == 200:
            res = json.loads(body)
            api_data = res.get("data")

            result = [{
                "tax_code": api_data["taxCode"],
                "company_name": api_data["companyName"],
                "company_address": api_data["address"],
                "company_industry": api_data["businessType"],
                "company_active_status": api_data["activeStatus"]
            }]
            check_data = "True"
        elif status_code == 201:
            return {
                "instruction": f"Mã số thuế {taxCode} không hợp lệ hoặc không tồn tại có thể do đang thực hiện thủ tục đăng ký với cơ quan thuế. Bạn vui lòng kiểm tra và cung cấp lại thông tin.",
                "data": [{}],
                "answer_format": "",
                "check_data": check_data,
                "function_calling": {
                    "name": "",
                    "natural_name": "",
                    "params": [],
                    "category": "",
                    "relevant_functions": [{"name": "", "alias": ""}]
                },
            }
        else:
            return {
                "instruction": "Đã có lỗi xảy ra, vui lòng thử lại",
                "data": [{}],
                "answer_format": "",
                "check_data": check_data,
                "function_calling": {
                    "name": "",
                    "natural_name": "",
                    "params": [],
                    "category": "",
                    "relevant_functions": [{"name": "", "alias": ""}]
                },
            }

        # Tạo hướng dẫn và định dạng câu trả lời
        instruction = """
        Dựa trên answer_format để đưa ra câu trả lời.
        """.strip()

        answer_format = """
        Format câu trả lời:
        Thông tin Mã số thuế "...":
        - Tên công ty:
        - Địa chỉ:
        - Ngành nghề chính:
        - Tình trạng hoạt động:
        Anh/chị có muốn thêm khách hàng không?
        """.strip()

        if result == [{}]:
            check_data = "False"

        # Trả về kết quả
        return {
            "instruction": instruction,
            "data": result,
            "answer_format": answer_format,
            "check_data": check_data,
            "function_calling": {
                "name": "",
                "natural_name": "",
                "params": [],
                "category": "action",
                "relevant_functions": [{"name": "Thêm khách hàng", "alias": "Thêm khách hàng"}]
            },
        }

    except Exception as e:
        # Xử lý ngoại lệ
        print(f"Error occurred while calling API: {e}")
        return {
            "result": "error",
            "message": "Đã xảy ra lỗi khi gọi API.",
            "data": [{}]
        }


# Hàm xử lý cho flow = 3
def handle_flow_3(data: list) -> dict:
    """Xử lý logic cho flow = 3"""
    relevant_functions = [
        {"name": "Xem chi tiết Ao cơ hội", "alias": "Xem chi tiết Ao cơ hội"}]

    # Kiểm tra trạng thái "OpportunityPoolStatus" trong dữ liệu
    if data and "OpportunityPoolStatus" in data[0]:
        if data[0]["OpportunityPoolStatus"] == "Lead chưa được xử lý":
            relevant_functions = [
                {"name": "Xem chi tiết Ao cơ hội",
                    "alias": "Xem chi tiết Ao cơ hội"},
                {"name": "Nhận xử lý ao cơ hội", "alias": "Nhận xử lý ao cơ hội"}
            ]

    # Tạo hướng dẫn và định dạng câu trả lời
    instruction = """
    Dựa trên answer_format để đưa ra câu trả lời.
    """.strip()

    answer_format = """
    Format câu trả lời:
    MST <mã số thuế> - Công ty <tên khách hàng trên ao cơ hội> quan tâm đến sản phẩm <tên sản phẩm trên ao cơ hội> vào ngày <ngày trên ao cơ hội> trên Ao cơ hội, tình trạng <tình trạng trên ao cơ hội>.
    """.strip()

    # Trả về kết quả
    return {
        "result": "success",
        "instruction": instruction,
        "data": data[:1],  # Lấy 1 phần tử đầu tiên từ danh sách dữ liệu
        "answer_format": answer_format,
        "function_calling": {
            "name": "",
            "natural_name": "",
            "params": [],
            "category": "action",
            "relevant_functions": relevant_functions
        },
    }

# Hàm xử lý cho flow = 4


def handle_flow_4(data: list) -> dict:
    """Xử lý logic cho flow = 4"""
    relevant_functions = [
        {"name": "Xem chi tiết tiềm năng", "alias": "Xem chi tiết tiềm năng"}]

    # Kiểm tra trạng thái "IsConverted" trong dữ liệu
    if data and "IsConverted" in data[0] and data[0]["IsConverted"] == False:
        relevant_functions = [
            {"name": "Chuyển đổi tiềm năng", "alias": "Chuyển đổi tiềm năng"},
            {"name": "Xem chi tiết tiềm năng", "alias": "Xem chi tiết tiềm năng"}
        ]

    # Tạo hướng dẫn và định dạng câu trả lời
    instruction = """
    Dựa trên answer_format để đưa ra câu trả lời.
    """.strip()

    answer_format = """
    Format câu trả lời:
    MST <mã số thuế> của công ty <tên khách hàng>, Người liên hệ <tên liên hệ>, Chức danh<chức danh>, SĐT liên hệ <số điện thoại liên hệ> được cập nhật trên Tiềm năng MST chưa là KH của MISA.
    """.strip()

    # Trả về kết quả
    return {
        "result": "success",
        "instruction": instruction,
        "data": data[:1],  # Lấy 1 phần tử đầu tiên từ danh sách dữ liệu
        "answer_format": answer_format,
        "function_calling": {
            "name": "",
            "natural_name": "",
            "params": [],
            "category": "action",
            "relevant_functions": relevant_functions
        },
    }

# Hàm xử lý cho flow = 5


def handle_flow_5(data: list) -> dict:
    """Xử lý logic cho flow = 5"""
    relevant_functions = [
        {"name": "Gợi ý chào bán sản phẩm", "alias": "Gợi ý chào bán sản phẩm"},
        {"name": "Tra cứu thông tin liên hệ", "alias": "Tra cứu thông tin liên hệ"}
    ]

    # Tạo hướng dẫn và định dạng câu trả lời
    instruction = """
    Dựa trên answer_format để đưa ra câu trả lời.
    """.strip()

    answer_format = """
    Format câu trả lời:
    Thông tin Mã số thuế "...":
    - Tên công ty:
    - Địa chỉ:
    - Ngành nghề chính:
    - Tình trạng hoạt động:
    KH này chưa quan tâm sản phẩm nào của MISA. 
    """.strip()

    # Trả về kết quả
    return {
        "result": "success",
        "instruction": instruction,
        "data": data[:1],  # Lấy 1 phần tử đầu tiên từ danh sách dữ liệu
        "answer_format": answer_format,
        "function_calling": {
            "name": "",
            "natural_name": "",
            "params": [],
            "category": "action",
            "relevant_functions": relevant_functions
        },
    }


# Hàm xử lý cho flow = 6
def handle_flow_6(data: list) -> dict:
    """Xử lý logic cho flow = 6"""
    relevant_functions = [
        {"name": "Lịch sử hoạt động", "alias": "Lịch sử hoạt động"},
        {"name": "Lịch sử chăm sóc KH", "alias": "Lịch sử chăm sóc KH"},
        {"name": "Gợi ý chào bán sản phẩm", "alias": "Gợi ý chào bán sản phẩm"},
        {"name": "Tra cứu thông tin liên hệ", "alias": "Tra cứu thông tin liên hệ"}
    ]

    # Tạo hướng dẫn và định dạng câu trả lời
    instruction = """
    Dựa trên answer_format để đưa ra câu trả lời.
    """.strip()

    answer_format = """
    Format câu trả lời:
    Mã số thuế trên đã tồn tại trên hệ thống.
    KH đã quan tâm sản phẩm này.
    """.strip()

    # Trả về kết quả
    return {
        "result": "success",
        "instruction": instruction,
        "data": data[:1],  # Lấy 1 phần tử đầu tiên từ danh sách dữ liệu
        "answer_format": answer_format,
        "function_calling": {
            "name": "",
            "natural_name": "",
            "params": [],
            "category": "action",
            "relevant_functions": relevant_functions
        },
    }


# Hàm xử lý cho flow = 7
def handle_flow_7(data: list) -> dict:
    """Xử lý logic cho flow = 7"""
    relevant_functions = [
        {"name": "Lịch sử hoạt động", "alias": "Lịch sử hoạt động"},
        {"name": "Lịch sử chăm sóc KH", "alias": "Lịch sử chăm sóc KH"},
        {"name": "Gợi ý chào bán sản phẩm", "alias": "Gợi ý chào bán sản phẩm"},
        {"name": "Tra cứu thông tin liên hệ", "alias": "Tra cứu thông tin liên hệ"},
        {"name": "Doanh thu/quy mô nhân sự", "alias": "Doanh thu/quy mô nhân sự"},
        {"name": "Thêm cơ hội", "alias": "Thêm cơ hội"}
    ]

    # Tạo hướng dẫn và định dạng câu trả lời
    instruction = """
    Dựa trên answer_format để đưa ra câu trả lời.
    """.strip()

    answer_format = """
    Format câu trả lời:
    Thông tin Mã số thuế "...":
    - Tên công ty:
    - Địa chỉ:
    - Ngành nghề chính:
    - Tình trạng hoạt động:
    KH đang tìm hiểu bộ sản phẩm "Tên sản phẩm trên phân hệ KD" từ ngày  <ngày trên KH >, trước đó KH đã tìm hiểu sản phẩm <tên sản phẩm khác trên khách hàng> ngày <ngày sinh cơ hội thất bại>. 
    KH đã mua sản phẩm (Tên đơn hàng)- thêm user - KD chăm sóc
    """.strip()

    # Trả về kết quả
    return {
        "result": "success",
        "instruction": instruction,
        "data": data[:1],  # Lấy 1 phần tử đầu tiên từ danh sách dữ liệu
        "answer_format": answer_format,
        "function_calling": {
            "name": "",
            "natural_name": "",
            "params": [],
            "category": "action",
            "relevant_functions": relevant_functions
        },
    }


# Hàm xử lý cho flow = 99
def handle_flow_99(data: list) -> dict:
    return {
        "result": "error",
        "message": "Có lỗi xảy ra khi tra cứu MST.",
        "data": data
    }
