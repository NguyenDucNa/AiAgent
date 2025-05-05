import re
import traceback
import requests
import json
# from example.ava_example.src.config import settings
from langchain_core.tools import tool
from pydantic import Field, BaseModel

import json
import re


class Input(BaseModel):
    """
    Sử dụng để lấy nội dung từ các links
    """
    urls: str = Field(
        ...,
        description="Danh sách các liên kết dưới dạng chuỗi JSON.",
        example='["https://example.com", "https://example2.com"]',
    )


@tool("MisaCrmGetContentFromUrl", args_schema=Input, return_direct=False)
def MisaCrmGetContentFromUrl(urls: str) -> dict:
    """
    Lấy nội dung từ các liên kết
    """
    url = "https://test-aiservice.misa.com.vn/clean-html/api/v1/process"

    # Chuyển đổi chuỗi JSON thành danh sách Python
    try:
        # Chuyển từ chuỗi JSON sang danh sách Python
        urls_list = json.loads(urls)
        if not isinstance(urls_list, list):
            raise ValueError("Input 'urls' phải là một danh sách JSON hợp lệ.")
    except json.JSONDecodeError:
        return {
            "results": "Error: 'urls' phải là một chuỗi JSON hợp lệ.",
            "instruction": ""
        }
    except ValueError as e:
        return {
            "results": f"Error: {str(e)}",
            "instruction": ""
        }

    json_data = {
        "urls": urls_list,
        "chunk": False,
        "chunk_size": 3000,
    }

    try:
        # Thêm timeout để tránh treo
        response = requests.post(url, json=json_data, timeout=10)

        # Kiểm tra mã trạng thái HTTP
        if response.status_code != 200:
            return {
                "results": f"Error: API trả về mã trạng thái {response.status_code}.",
                "instruction": ""
            }

        data = response.json()
        # Debug phản hồi từ API
        print(
            f"Debug: API response: {json.dumps(data, indent=2, ensure_ascii=False)}")

        # Kiểm tra và xử lý phản hồi dựa trên trường "items"
        if "items" in data and isinstance(data["items"], list):
            items = data["items"]
            processed_items = [{"Title": item.get("title", "No Title"), "Content": item.get(
                "content", "No Content")} for item in items]
            return {
                "results": json.dumps(processed_items, ensure_ascii=False, indent=2),
                "instruction": "Nếu người dùng yêu cầu tóm tắt link này, thì hãy tóm tắt từng phần của bài viết."
            }
        else:
            return {
                "results": "Error: Phản hồi từ API không chứa trường 'items' hoặc không hợp lệ.",
                "instruction": ""
            }
    except requests.exceptions.ConnectionError:
        return {
            "results": "Không thể kết nối đến API. Vui lòng kiểm tra URL hoặc kết nối mạng.",
            "instruction": ""
        }
    except requests.exceptions.Timeout:
        return {
            "results": "Kết nối đến API bị timeout. Vui lòng thử lại sau.",
            "instruction": ""
        }
    except requests.exceptions.RequestException as e:
        return {
            "results": f"Lỗi khi gọi API: {str(e)}",
            "instruction": ""
        }


if __name__ == "__main__":
    # Test the function
    urls = '["https://www.wikipedia.org", "https://www.example.com"]'  # Chuỗi JSON
    result = MisaCrmGetContentFromUrl(urls)
    print(result)
