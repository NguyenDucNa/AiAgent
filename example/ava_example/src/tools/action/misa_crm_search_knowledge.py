# import traceback
# from src.config import settings
# from langchain_core.tools import tool
# from pydantic import Field, BaseModel


# class Input(BaseModel):
#     product_name: str = Field(
#         ...,
#         description="Tên sản phẩm"
#     )
#     user_message: str = Field(
#         ...,
#         description="Tin nhắn của người dùng"
#     )


# @tool("MisaCrmSearchKnowledge", args_schema=Input, return_direct=False)
# def MisaCrmSearchKnowledge(
#     product_name: str,
#     user_message: str,

# ):
#     """Sử dụng tools này để tìm kiếm thông tin sản phẩm trên CRM Misa"""

#     print(" ====================== MisaCrmSearchKnowledge ===================")


#     # Node HTTP request
#     import requests
#     url = "https://aiservice.misa.vn/chatbot-api/v1/search"
#     headers = {
#         "api-key": "AI_team",
#         "app": "CRMMISA",
#         "Content-Type": "application/json"
#     }

#     json_data = {
#         "question": user_message,
#         "document_db": "ava_CRMMISAJSC_document",
#         "top_k_doc": 10,
#         "embedding_engine": "llm",
#         "embedding_threshold": 0.0,
#         "filter": {"product_code":[product_name]},
#         "question_db": "ava_CRMMISAJSC_question",
#         "top_k_question": 10,
#         "question_threshold": 0.88,
#         "faq_db": "ava_CRMMISAJSC_faq",
#         "faq_threshold": 0.88,
#         "general_db": "ava_misa_general",
#         "general_threshold": 0,
#         "status": 0,
#         "vector_name": "vectors",
#         "qdrant_db": "test",
#     }



#     response = requests.post(url, headers=headers, json=json_data)
#     status_code = response.status_code
#     print(f"Response status code: {status_code}")
#     print(f"Response content: {response.content}")
#     if status_code != 200:
#         return {
#             "result": "error",
#             "note": "Trả lời xin lỗi hiện tại không lấy được thông tin này."
#         }
#     items = response.json()
    

#     import json
#     import re

#     HIGH_CONF_SCORE = 0.5
#     LOW_CONF_SCORE = 0.4
#     FILE_HIGH_CONF_SCORE = 0.35
#     FILE_LOW_CONF_SCORE = 0.3

#     def parse_hit_docs(hit_docs: list[dict]) -> list[dict]:
#         parsed_items: list[dict] = []
#         for item in hit_docs:
#             payload: dict = item.get("payload", {})
#             source: str = (
#                 payload.get("short_link", "") or
#                 payload.get("source", "")
#             )
#             parsed_items.append(
#                 {
#                     "id": item["id"],
#                     "collection_name": item["collection_name"],
#                     "score": item["score"],
#                     "answer": payload.get("answer", ""),
#                     "title": payload.get("title", ""),
#                     "content": payload.get("content", ""),
#                     "type": detect_source_type(source),
#                     "source": clean_source(source),
#                     "product_code": payload.get("product_code", []),
#                     "subsystem_id": payload.get("subsystem_id", []),
#                     "lookup_link": payload.get("lookup_link", "")
#                 }
#             )
#         return parsed_items

#     def clean_source(source: str) -> str:
#         if isinstance(source, str):
#             for prefix in ["custom:", "link:", "file:", "faq:"]:
#                 if source.startswith(prefix):
#                     return source[len(prefix):].strip()
#         return source
        
#     def detect_source_type(source: str) -> str:
#         if isinstance(source, str):
#             if (
#                 source.startswith("link:") or
#                 re.match(r'^https?://[^ ]+$', source)
#             ):
#                 return "link"
#             elif source.startswith("file:"):
#                 return "file"
#             elif source.startswith("faq:"):
#                 return "faq"
#         return "custom"

#     def is_low_confidence_item(item: dict) -> bool:
#         upper_threshold = HIGH_CONF_SCORE
#         lower_threshold = LOW_CONF_SCORE
#         if item["type"] == "file":
#             upper_threshold = FILE_HIGH_CONF_SCORE
#             lower_threshold = FILE_LOW_CONF_SCORE
#         return lower_threshold <= item["score"] < upper_threshold

#     def is_high_confidence_item(item: dict) -> bool:
#         upper_threshold = HIGH_CONF_SCORE
#         if item["type"] == "file":
#             upper_threshold = FILE_HIGH_CONF_SCORE
#         return item["score"] >= upper_threshold

#     if status_code == 200:
#         if items and isinstance(items, list) and isinstance(items[0], list):
#             items = items[0] + items[1]
#         items = parse_hit_docs(items)
#     else:
#         items = []

#     if items and items[0].get("answer"):
#         instruction = ""
#         return {
#             "items": [
#                 {
#                     "answer": items[0]["answer"],
#                     "use_case": "faq_knowledge"
#                 }
#             ],
#             "note": instruction
#         }
#     else:
#         high_conf_items = []
#         low_conf_items = []
#         for item in items:
#             if is_high_confidence_item(item):
#                 item["use_case"] = "high_confidence_knowledge"
#                 high_conf_items.append(item)
#             elif is_low_confidence_item(item):
#                 item["use_case"] = "low_confidence_knowledge"
#                 low_conf_items.append(item)

#         instruction: str = """
# Nhiệm vụ của bạn là đưa ra câu trả lời cho người dùng dựa trên các tài liệu tham khảo trong `results`.
# 1. Không trả về markdown trong câu trả lời, chỉ trả về văn bản thuần. Phải trả về kèm theo link nếu câu trả lời có dẫn link.
# 2. Trả lời đúng trọng tâm vấn đề trong câu hỏi của người dùng dựa trên kết quả tìm tri thức.
# 3. Nếu không tìm được tài liệu tham khảo hoặc tài liệu tham khảo không có thông tin để trả lời thì bạn hãy sử dụng kiến thức của bản thân để trả lời. Nhưng phải trích dẫn cho người dùng đây là "câu trả lời tham khảo từ ChatGPT. Ví dụ: "Mình chưa có tri thức từ MISA để trả lời, tuy nhiên bạn có thể tham khảo nguồn sau từ ChatGPT....".""".strip()
    
#     print(items)
#     return {
#         "items": high_conf_items or low_conf_items,
#         "note": instruction
#     }
    
