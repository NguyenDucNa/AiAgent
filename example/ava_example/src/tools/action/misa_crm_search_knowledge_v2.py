import re
import traceback
import requests
import json
# from example.ava_example.src.config import settings
from langchain_core.tools import tool
from pydantic import Field, BaseModel

import json
import re

HIGH_CONF_SCORE = 0.5
LOW_CONF_SCORE = 0.4
# FILE_HIGH_CONF_SCORE = 0.4
FILE_LOW_CONF_SCORE = 0.3


class Input(BaseModel):
    query: str = Field(
        ...,
        description="Query used to search knowledge"
    )
    products: str = Field(
        ...,
        description="Tên (các) sản phẩm người dùng đang phụ trách hoặc cần tìm kiếm tài liệu tham khảo, chỉ nhận giá trị từ danh sách sau: MAKT, CRM, ME, Inbot, SME, all, none. Nếu không có thông tin về sản phẩm hoặc người dùng chưa cung cấp thì hỏi lại người dùng; nếu có nhiều sản phẩm thì các sản phẩm phân cách nhau bởi dấu phẩy (,). Trong đó:\nMAKT - AMIS Kế toán là phần mềm kế toán, bao gồm các keyword như MAKT, AMIS Kế toán, ...;\nCRM - AMIS Bán hàng là phần mềm bán hàng, bao gồm các keyword như CRM, Bán hàng, AMIS CRM, ...;\nME - Hoá đơn đầu ra là phần mềm hóa đơn đầu ra, bao gồm các keyword như meInvoice, MEI, ...;\nInbot - Hoá đơn đầu vào là phần mềm xử lý hóa đơn đầu vào, bao gồm các keyword như Inbot, InvoiceBot;\nSME - MISA SME là phần mềm kế toán desktop, bao gồm các keyword như SME, sme 2023, ..."
    )
    does_search_from_help_link: bool = Field(
        ...,
        description="Nếu muốn tìm tri thức hướng dẫn sử dụng phần mềm hoặc help hướng dẫn thì does_search_from_help_link có giá trị (Yes), nếu Muốn tìm tất cả các tri thức khác thì nhận giá trị No"
    )


def call_api_knowledge(query: str, products: list[str]) -> dict:
    """
    Gọi API để tìm kiếm tri thức khi có nhiều sản phẩm được cung cấp.

    Args:
        query (str): Câu truy vấn tìm kiếm.
        products (list[str]): Danh sách các sản phẩm.

    Returns:
        dict: Kết quả trả về từ API sau khi xử lý.
    """
    url = "https://test-aiservice.misa.com.vn/chatbot-api/v1/search"
    headers = {
        "api-key": "AI_team",
        "app": "CRMMISAJSC",
        "Content-Type": "application/json"
    }
    json_data = {
        "question": query,
        "document_db": "ava_CRMMISAJSC_document",
        "top_k_doc": 10,
        "embedding_engine": "llm",
        "embedding_threshold": 0.0,
        "filter": {"product_code": products[0]} if products else {},  # Correct structure
        "question_db": "ava_CRMMISAJSC_question",
        "top_k_question": 5,
        "question_threshold": 0.88,
        "faq_db": "ava_CRMMISAJSC_faq",
        "faq_threshold": 0.88,
        "general_db": "ava_misa_general",
        "general_threshold": 0,
        "status": 0,
        "vector_name": "vectors",
        "qdrant_db": "production"
    }

    try:
        print(f"Calling API with query: {query} and products: {products}")
        response = requests.post(url, headers=headers, json=json_data)
        response.raise_for_status()
        api_result = response.json()

        # Ensure the response is a dictionary
        if isinstance(api_result, list):
            return {"status": 200, "body": json.dumps(api_result)}  # Wrap list in a dictionary
        return api_result

    except requests.RequestException as e:
        raise RuntimeError(f"Lỗi khi gọi API: {e}")


def parse_hit_docs_nor(hit_docs: list[dict]) -> list[dict]:
    """
    Parse and simplify the raw API response data.

    Args:
        hit_docs (list[dict]): Raw data from the API.

    Returns:
        list[dict]: Simplified and structured data.
    """
    parsed_items: list[dict] = []
    for item in hit_docs:
        payload: dict = item.get("payload", {})
        source: str = (
            payload.get("short_link", "") or
            payload.get("source", "")
        )
        parsed_items.append(
            {
                "id": item.get("id", ""),
                "collection_name": item.get("collection_name", ""),
                "score": item.get("score", 0),
                "answer": payload.get("content", ""),  # Main content
                "title": payload.get("title", ""),  # Title of the document
                "type": detect_source_type(source),  # Type of the source
                "source": clean_source(source),  # Cleaned source
                "product_code": payload.get("product_code", ""),  # Product code
                "lookup_link": payload.get("lookup_link", ""),  # Lookup link if available
            }
        )
    return parsed_items

def parse_hit_docs_with_product(hit_docs: list[dict], product: str) -> list[dict]:
    parsed_items: list[dict] = []
    for item in hit_docs:
        payload: dict = item.get("payload", {})
        source: str = (
            payload.get("short_link", "") or
            payload.get("source", "")
        )
        parsed_items.append(
            {
                "id": item["id"] or "",
                "collection_name": item.get("collection_name") or "",
                "score": item.get("score") or 0,
                "answer": payload.get("answer") or "",
                "title": payload.get("title") or "",
                "content": payload.get("content") or "",
                "type": detect_source_type(source),
                "source": clean_source(source) or "",
                "subsystem_id": payload.get("subsystem_id") or [],
                "lookup_link": payload.get("lookup_link") or "",
                "product_code": product
            }
        )
    return parsed_items


def clean_source(source: str) -> str:
    if isinstance(source, str):
        for prefix in ["custom:", "link:", "file:", "faq:"]:
            if source.startswith(prefix):
                return source[len(prefix):].strip()
    return source


def detect_source_type(source: str) -> str:
    if isinstance(source, str):
        if (
            source.startswith("link:") or
            re.match(r'^https?://[^ ]+$', source)
        ):
            return "link"
        elif source.startswith("file:"):
            return "file"
        elif source.startswith("faq:"):
            return "faq"
    return "custom"


def is_low_confidence_item(item: dict, upper: float) -> bool:
    upper_threshold = HIGH_CONF_SCORE
    lower_threshold = LOW_CONF_SCORE
    if item["type"] == "file":
        upper_threshold = upper
        lower_threshold = FILE_LOW_CONF_SCORE
    return lower_threshold <= item["score"] < upper_threshold


def is_high_confidence_item(item: dict, upper: float) -> bool:
    upper_threshold = HIGH_CONF_SCORE
    if item["type"] == "file":
        upper_threshold = upper
    return item["score"] >= upper_threshold


@tool("MisaCrmSearchKnowledgeV2", args_schema=Input, return_direct=False)
def MisaCrmSearchKnowledgeV2(
    query: str,
    products: str,
    does_search_from_help_link: bool
):
    """Sử dụng tool này để tra cứu tri thức, tài liệu liên quan đến:
- Từ điển theo lĩnh vực và ngành nghề;
- Các tình huống về chào hàng, bán hàng và hướng dẫn xử lý khi khách hàng từ chối, khen chê, ...;
- Các tính năng nổi bật, các lợi ích đi kèm;
- Am hiểu về các đối thủ cạnh tranh;
- Các tài liệu khác về tư vấn nhân viên kinh doanh bán hàng.

**Bắt buộc gọi vào tool này để lấy thông tin trả lời cho tất cả các câu hỏi của người dùng nếu không chọn tool khác.**

Sử dụng tool này để tra cứu tri thức, tài liệu liên quan đến:
- Từ điển theo lĩnh vực và ngành nghề;
- Các tình huống về chào hàng, bán hàng và hướng dẫn xử lý khi khách hàng từ chối, khen chê, ...;
- Các tính năng nổi bật, các lợi ích đi kèm;
- Am hiểu về các đối thủ cạnh tranh;
- Các tài liệu khác về tư vấn nhân viên kinh doanh bán hàng.

**Bắt buộc gọi vào tool này để lấy thông tin trả lời cho tất cả các câu hỏi của người dùng nếu không chọn tool khác.**
"""

    print(" ====================== MisaCrmSearchKnowledgeV2 ===================")

    if not products:
        products = "MAKT"
    products: str = products.strip()
    if products in ["all", "none"]:
        products = ""

    instruction: str = ""
    if products:
        products: list[str] = [e.strip() for e in products.split(",")]
    else:
        products: list[str] = []
        instruction = "Bạn cần yêu cầu người dùng cung cấp tên sản phẩm"

    num_products = len(products)

    # Add logic to handle cases based on the number of products
    if num_products == 0:
        instruction = "Không có sản phẩm nào được cung cấp. Vui lòng yêu cầu người dùng cung cấp tên sản phẩm."
    elif num_products == 1:
        if does_search_from_help_link:
            help_data = help_link_true(products[0], query)
            return help_data
        else:
            help_link_false_result = help_link_false(query,products)
            return help_link_false_result
    else:
        num_product_default_result = num_product_default(products, query)
        return num_product_default_result
    
def help_link_false(query: str, products: list[str]) -> dict:
    api_result = call_api_knowledge(query, products)
    status_code: int = api_result.get("status", 0)
    mapping_product: dict = {
        "MAKT": "MAKT",
        "ME": "ME",
        "CRM": "crm",
        "Inbot": "Invbot",
        "SME": "sme"
    }
    help_db: str = mapping_product[products[0]] if products[0] in mapping_product else ""
    help_document_db: str = f"ava_{help_db}_document"
    help_question_db: str = f"ava_{help_db}_question"
    help_faq_db: str = f"ava_{help_db}_faq"

    instruction: str = ""

    # Initialize items properly
    items = []

    if status_code == 200:
        # Parse the API response body
        body = api_result.get("body", "[]")
        items = json.loads(body)
        if items and isinstance(items, list) and isinstance(items[0], list):
            items = items[0] + items[1]
        items = parse_hit_docs_nor(items)  # Process the items

        # Debug: Add this line to inspect parsed items
        parsed_items = parse_hit_docs_nor(items)
    else:
        items = []

    if items and items[0].get("answer"):
        return {
            "items": [
                {
                    "answer": items[0]["answer"],
                    "use_case": "faq_knowledge"
                }
            ],
            "note": instruction,
            "help_document_db": help_document_db,
            "help_question_db": help_question_db,
            "help_faq_db": help_faq_db,
            "help_db": help_db
        }

    else:
        high_conf_items = []
        low_conf_items = []
        for item in items:
            if is_high_confidence_item(item, upper=0.4):
                item["use_case"] = "high_confidence_knowledge"
                high_conf_items.append(item)
            elif is_low_confidence_item(item, upper=0.4):
                item["use_case"] = "low_confidence_knowledge"
                low_conf_items.append(item)

        instruction = """
Your task is to provide a clear and concise answer based on the knowledge database stored in `results`.
1. Use only plain text, no markdown. Include links if referenced.  
2. Focus strictly on the user's question and answer only what is asked.  
3. The answer MUST be concise and structured according to the headings in the references, preserving the original titles or indexes (e.g., if the title of a step is "Bước 10. ABC," you MUST keep exactly "Bước 10. ABC").
4. If you cannot find a reference or the reference does not have information to answer, please use your own knowledge to answer. But you must cite to the user that this is a "reference answer from ChatGPT. For example: "Hiện tại mình chưa có tri thức của MISA để trả lời, nhưng bạn có thể tham khảo câu trả lời sau từ ChatGPT......" """.strip()

    return {
        "items": high_conf_items + low_conf_items,
        "note": instruction,
        "help_document_db": help_document_db,
        "help_question_db": help_question_db,
        "help_faq_db": help_faq_db,
        "help_db": help_db
    }
def help_link_true(product: str, query: str) -> dict:
    mapping_product: dict = {
        "MAKT": "MAKT",
        "ME": "ME",
        "CRM": "crm",
        "Inbot": "Invbot",
        "SME": "sme"
    }
    help_db: str = mapping_product[product]
    help_document_db: str = f"ava_{help_db}_document"
    help_question_db: str = f"ava_{help_db}_question"
    help_faq_db: str = f"ava_{help_db}_faq"
    url = "https://aiservice.misa.vn/chatbot-api/v1/search"
    headers = {
        "api-key": "AI_team",  # Ensure this is correct
        "app": help_db,
        "Content-Type": "application/json"
    }
    json_data = {
        "question": query,
        "document_db": help_document_db,
        "top_k_doc": 10,
        "embedding_engine": "llm",
        "embedding_threshold": 0.0,
        "filter": {},
        "question_db": help_question_db,
        "top_k_question": 5,
        "question_threshold": 0.88,
        "faq_db": help_faq_db,
        "faq_threshold": 0.88,
        "general_db": "ava_misa_general",
        "general_threshold": 0,
        "status": 0,
        "vector_name": "vectors",
        "qdrant_db": "production"
    }


    try:
        response = requests.post(url, headers=headers, json=json_data)
        response.raise_for_status()
        api_result = response.json()

         # Handle list response
        if isinstance(api_result, list):
            api_result = {"status": 200, "body": json.dumps(api_result)}

        status_code: int = api_result.get("status", 0)

        instruction: str = """Không trả về markdown trong câu trả lời, chỉ trả về văn bản thuần. Phải trả về kèm theo link nếu câu trả lời có dẫn link. Chỉ dựa trên các tài liệu tham khảo trong `results` để đưa ra câu trả lời. Nếu không tìm được tài liệu nào hoặc các tài liệu tìm được đều không phù hợp, bạn hãy sử dụng tri thức của bản thân để trở lời, tuy nhiên phải kèm theo trích dẫn "tham khảo câu trả lời từ ChatGPT". For example: "Hiện tại mình chưa có tri thức của MISA để trả lời, nhưng bạn có thể tham khảo câu trả lời sau từ ChatGPT....."
        """

        if status_code == 200:
            items = json.loads(api_result.get("body", "[]"))
            if items and isinstance(items, list) and isinstance(items[0], list):
                items = items[0] + items[1]
            items = parse_hit_docs_with_product(items, product)
        else:
            items = []

        if items and items[0].get("answer"):
            return {
                "items": [
                    {
                        "answer": items[0]["answer"],
                        "use_case": "faq_knowledge"
                    }
                ],
                "note": instruction
            }
        else:
            high_conf_items = []
            low_conf_items = []
            for item in items:
                if is_high_confidence_item(item, upper=0.35):
                    item["use_case"] = "high_confidence_knowledge"
                    high_conf_items.append(item)
                elif is_low_confidence_item(item, upper=0.35):
                    item["use_case"] = "low_confidence_knowledge"
                    low_conf_items.append(item)
            return {
                "items": high_conf_items + low_conf_items,
                "note": instruction
            }

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            raise RuntimeError("Unauthorized: Please check your API key and permissions.")
        else:
            raise RuntimeError(f"HTTP Error: {e}")
    except requests.RequestException as e:
        raise RuntimeError(f"Lỗi khi gọi API: {e}")




def num_product_default(products: str, query: str) -> dict:
    api_result = call_api_knowledge(query, products)
    instruction: str = ""
    status_code: int = api_result.get("status", 0)
    body: str = api_result.get("body", "")

    items: list[dict] = []

    if status_code == 200:
        all_items: list = json.loads(body)
        if all_items and isinstance(all_items, list) and isinstance(all_items[0], list):
            all_items = all_items[0] + all_items[1]
        items = [item for item in all_items if item.get(
            "payload", {}).get("product_code") in products]
        items = parse_hit_docs_nor(items)

    if items and items[0].get("answer"):
        return {
            "items": [
                {
                    "answer": items[0]["answer"],
                    "use_case": "faq_knowledge"
                }
            ],
            "note": instruction
        }

    else:
        high_conf_items = []
        low_conf_items = []
        for item in items:
            if is_high_confidence_item(item, upper=0.35):
                item["use_case"] = "high_confidence_knowledge"
                high_conf_items.append(item)
            elif is_low_confidence_item(item):
                item["use_case"] = "low_confidence_knowledge"
                low_conf_items.append(item)

    #         instruction: str = """
    # Nhiệm vụ của bạn là đưa ra câu trả lời cho người dùng dựa trên các tài liệu tham khảo trong `results`.
    # 1. Không trả về markdown trong câu trả lời, chỉ trả về văn bản thuần. Phải trả về kèm theo link nếu câu trả lời có dẫn link.
    # 2. Trả lời đúng trọng tâm vấn đề trong câu hỏi của người dùng dựa trên kết quả tìm tri thức.
    # 3. Nếu tài liệu tham khảo không có thông tin để trả lời thì nhờ người dùng mô tả rõ hơn câu hỏi hoặc vấn đề.""".strip()
            instruction = """
    Your task is to provide a clear and concise answer based on the reference materials in `results`.  
    1. Use only plain text, no markdown. Include links if referenced.  
    2. Focus strictly on the user's question and answer only what is asked.
    3. If the reference contains headings other structured elements, MUST organize them in a parent-child relationship as in the original materials, and MUST keep the original titles or indexes of the headings if possible, for example, if the title of the step in the reference is "Bước 10. ABC", you MUST keep exactly "Bước 10. ABC" in your answer.
    4. If you cannot find a reference or the reference does not have information to answer, please use your own knowledge to answer. But you must cite to the user that this is a "reference answer from ChatGPT. For example: "Hiện tại mình chưa có tri thức của MISA để trả lời, nhưng bạn có thể tham khảo câu trả lời sau từ ChatGPT......" """.strip()

    return {
        "items": high_conf_items + low_conf_items,
        "note": instruction
    }


if __name__ == "__main__":
   res =  MisaCrmSearchKnowledgeV2(
    query = "kịch bản chào hàng sản phẩm amis kế toán",
    products = "amis kế toán",
    does_search_from_help_link = True
    )
   print(res)
