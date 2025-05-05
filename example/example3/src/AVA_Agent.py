from langchain_openai import ChatOpenAI
from settings.config import LLM_CONF
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage, ToolMessage
from langgraph.prebuilt import ToolNode
from example.example3.src.tools.getGoldAndWeather import GetGoldAndWeather
from example.example3.src.tools.getBirthday import GetBirthDay

# Bộ nhớ lưu State của Graph
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver() # sử dụng bộ nhớ mặc định của Langgraph, khi triển khai thực tế sẽ sử dụng Redis hoặc MongoDB

llm = ChatOpenAI(
    base_url=LLM_CONF["openai"]["base_url"],
    api_key=LLM_CONF["openai"]["api_key"],
    model=LLM_CONF["openai"]["model"],
    # temperature=0,
    # stream_usage=True,
)

tools = [GetGoldAndWeather, GetBirthDay]
llm = llm.bind_tools(tools)

class State(TypedDict):
    # messages sẽ lưu trữ các tin nhắn của người dùng và AVA trong 1 turn hỏi - đáp
    messages: Annotated[list, add_messages] # hàm add_messages sẽ tự động thêm các tin nhắn vào messages khi node trả về một tin nhắn mới


graph_builder = StateGraph(State)

AVA_PROMPT = """Bạn là AVA, trợ lý số của công ty Cổ phần MISA. Nhiệm vụ của bạn là giải đáp các thắc mắc của người dùng.
Hôm nay là thứ Tư ngày 16 tháng 4 năm 2025."""

# Tất cả các node trong Langgraph sẽ nhận vào một State, và trả về giá trị update cho State.
def chatbot(state: State):
    return {"messages": [llm.invoke([SystemMessage(AVA_PROMPT)] + state["messages"])]}


graph_builder.add_node("AVA", chatbot)
graph_builder.add_node("tools", ToolNode(tools))
graph_builder.add_edge(START, "AVA")


def call_tool_or_stop(state):
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"

# Một số Tool sẽ trả về function_calling để dự án tự xử lý, khi đó không cần trả function_calling cho AVA
# Một số Tool khác (như hỏi thời tiết, giá vàng) thì cần trả kết quả về cho AVA trả lời người dùng
def back_to_agent_or_stop(state):
        messages = state["messages"]
        last_message = messages[-1]
        if "function_calling" in last_message.content:
            return "end"
        else:
            return "back"

graph_builder.add_conditional_edges("AVA", call_tool_or_stop, {"continue": "tools", "end": END})
graph_builder.add_conditional_edges("tools", back_to_agent_or_stop, {"back": "AVA", "end": END})


graph = graph_builder.compile(checkpointer=memory)
graph.get_graph().draw_mermaid_png(output_file_path="example/example3/src/graph.png")

session_id = "qwert"
config = {"configurable": {
    "thread_id": session_id,
    "user_id": "123456",
    "user_name": "Nguyễn Văn A"
    }}


def stream_graph_updates(user_input: str):
    for event in graph.stream(input={"messages": [{"role": "user", "content": user_input}]}, config=config):
        for value in event.values():
            content = value["messages"][-1].content
            role = "Tool" if isinstance(value["messages"][-1], ToolMessage) else "AVA"
            if content != '':
                print("="*50 + role + "="*50)
                print(role + ": ", content)

while True:
    try:
        print("="*50 + "User" + "="*50)
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