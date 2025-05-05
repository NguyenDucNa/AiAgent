from enum import Enum
from pydantic import BaseModel
from pymongo import MongoClient

from typing import TypedDict, Sequence, Union, Literal
from typing_extensions import Annotated

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.managed import IsLastStep, RemainingSteps
from langgraph.graph import StateGraph, END

from src.memory.mongodb.saver import MongoDBSaver
from src.config import settings

StructuredResponse = Union[dict, BaseModel]

class CustomerSupportSlots:
    """State dành riêng cho Customer Support Agent."""
    extracted_product_name: str = "amis_ke_toan"
    not_makt: bool = False
    hit_docs: list = []
    chitchat_count: int = 0
    ask_contact: bool = False  # Đánh dấu đã hỏi thông tin liên hệ
    phone_number: str = None  # Thêm trường lưu SĐT
    in_phone_flow: bool = False  # Đánh dấu đang trong luồng xử lý SĐT
    human_request_after_solution: int = 0  # Số lần yêu cầu gặp người sau khi cung cấp giải pháp
class UserInfo:
    """Thông tin người dùng."""
    user_phone: str
class ChatMetadata:
    """Metadata cho tin nhắn chat."""
    user_info: UserInfo
    product_name: str = "amis_ke_toan"

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]

    is_last_step: IsLastStep

    remaining_steps: RemainingSteps

    structured_response: StructuredResponse
    
    next: str

    template_id: str

    template_message: str
    
    negative_template_message: str
    
    cache_message: str
    
    current: str = None
    
    enable_cache: bool = False
    
    cache_key: str = None
    
    cache_age: int = None

    is_templated_anwser: bool = False

    chat_metadata: ChatMetadata = None
    
    customer_support_slots: CustomerSupportSlots = None

    """
    Monitor cache:
    0 || None: Không cache, template
    1: Cache kết quả trả về
    2: Câu trả lời sử dụng template
    TODO: Câu trả lời được cache dữ liệu call tool cần bổ sung thêm trường thông tin
    """
    cache_audit: int = None

class GraphConfig(TypedDict):
    model_name: Literal["openai", "anthropic", "slm-general"]


class  BaseGraph:
    def __init__(self, call_model, should_continue, action_to_agent_condition, tool_node):
        """
        Khởi tạo lớp cơ sở cho đồ thị.

        :param call_model: Hàm gọi model.
        :param should_continue: Hàm kiểm tra điều kiện tiếp tục.
        :param tool_node: Hàm thực thi công cụ.
        """
        self.call_model = call_model
        self.should_continue = should_continue
        self.action_to_agent_condition = action_to_agent_condition
        self.tool_node = tool_node

        
        client = MongoClient(settings.MONGO_CONF["connection"]["host"], 
                             username=settings.MONGO_CONF["connection"]["username"],
                             password=settings.MONGO_CONF["connection"]["password"])
        self.memory = MongoDBSaver(client, settings.MONGO_CONF["db_name"])


        # Khởi tạo đồ thị
        self.workflow = StateGraph(AgentState, config_schema=GraphConfig)

        # Thêm các node vào đồ thị
        self.workflow.add_node("agent", self.call_model)
        self.workflow.add_node("action", self.tool_node)

        # Thiết lập điểm bắt đầu
        self.workflow.set_entry_point("agent")

        # Thêm các cạnh có điều kiện
        self.workflow.add_conditional_edges(
            "agent",
            self.should_continue,
            {
                "continue": "action", #action
                "end": END,
            },
        )

        # Thêm cạnh thông thường
        # self.workflow.add_edge("action", "agent")
        self.workflow.add_conditional_edges(
            "action",
            self.action_to_agent_condition,   
            {
                "continue": "agent",
                "end": END,
            },
        )

        # Biên dịch đồ thị
        self.compiled_graph = self.workflow.compile(checkpointer=self.memory)

    def get_graph(self):
        """
        Trả về đồ thị đã biên dịch.
        """
        return self.compiled_graph
