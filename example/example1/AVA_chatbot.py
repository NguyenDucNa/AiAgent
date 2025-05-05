from langchain_openai import ChatOpenAI
from settings.config import LLM_CONF
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
import sys
import os

# Thêm thư mục gốc của project (AiAgent) vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


# Khởi tạo LLM sử dụng GPT-4o của OpenAI
llm = ChatOpenAI(
    base_url=LLM_CONF["openai"]["base_url"],
    api_key=LLM_CONF["openai"]["api_key"],
    model=LLM_CONF["openai"]["model"],
    # temperature=0,
    # stream_usage=True,
)

# Khai báo State của Graph. Một State lưu trữ thông tin của Graph qua mỗi bước xử lý.
# State trong ví dụ này chỉ một biến messages, lưu trữ các tin nhắn của người dùng và AVA trong 1 turn hỏi - đáp
class State(TypedDict):
    messages: Annotated[list, add_messages] # hàm add_messages sẽ tự động thêm các tin nhắn vào messages khi node trả về một tin nhắn mới


graph_builder = StateGraph(State)

AVA_PROMPT = """Bạn là AVA, trợ lý số của công ty Cổ phần MISA. Nhiệm vụ của bạn là giải đáp các thắc mắc của người dùng"""

# Tất cả các node trong Langgraph sẽ nhận vào một State, và trả về giá trị update cho State.
def chatbot(state: State):
    # hàm chatbot trả về messages của AVA, messages này sẽ được thêm vào messages của State nhờ hàm add_messages
    return {"messages": [llm.invoke([SystemMessage(AVA_PROMPT)] + state["messages"])]}


graph_builder.add_node("AVA", chatbot)
graph_builder.add_edge(START, "AVA")
graph_builder.add_edge("AVA", END)

graph = graph_builder.compile()


def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

"""Hãy thử chat với AVA, xem nó có nhớ được lịch sử chat không"""
while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "Bạn tên là gì?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break