from langgraph.pregel import Pregel
from langgraph.types import Command
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import  AIMessage, ToolMessage
from IPython.display import Image, display
from langchain_core.runnables.graph import CurveStyle, MermaidDrawMethod, NodeStyles
from langgraph.graph import StateGraph, START, END
from src.agent import (
    action_graph,
    general_graph
)
from src.agent.base import AgentState
from src.ai_core import (
    router_agent
)
from pymongo import MongoClient
from src.memory.mongodb.saver import MongoDBSaver
from src.config import settings

client = MongoClient(settings.MONGO_CONF["connection"]["host"], 
                             username=settings.MONGO_CONF["connection"]["username"],
                             password=settings.MONGO_CONF["connection"]["password"])
memory = MongoDBSaver(client, settings.MONGO_CONF["db_name"])


def supervisor_node(state: AgentState, config: RunnableConfig): 
    if isinstance(state["messages"][-1], AIMessage) and state["messages"][-1].content:
        return Command(goto=END, update={"next": END})

    goto = router_agent(state)

    if goto in ["general_node"]:
        return Command(goto=goto, update={"next": goto, "current": goto})
    else:
        return Command(
            goto=goto,
            update={
                "next": goto,
                "current": goto,
            },
        )


def generic_node(state: AgentState, node_name: str, graph: Pregel):
    """
    Hàm chung để xử lý các node khác nhau.

    :param state: Trạng thái hiện tại của đồ thị.
    :param node_name: Tên của node (ví dụ: "employees_node", "birthday_node").
    :param graph: Đồ thị tương ứng với node.
    :return: Trạng thái mới sau khi xử lý.
    """
    # Tạo một bản sao của trạng thái và lọc các tin nhắn liên quan đến node
    node_state = state.copy()
    node_state["messages"] = []
    for msg in state["messages"]:
        if isinstance(msg, AIMessage) and not msg.content and msg.name != node_name:
            continue
        if isinstance(msg, ToolMessage) and msg.name != node_name:
            continue
        node_state["messages"].append(msg)

    # Gọi đồ thị tương ứng
    results = graph.invoke(node_state)
    new_messages = results["messages"][len(node_state["messages"]) :]

    if results.get("customer_support_slots"):
        state["customer_support_slots"] = results.get("customer_support_slots")
    if results.get("chat_metadata"):
        state["chat_metadata"] = results.get("chat_metadata")
    # Cập nhật trạng thái với các tin nhắn mới
    new_state = state.copy()
    new_state["messages"] = state["messages"]
    ai_messages = {}
    for msg in state["messages"]:
        if isinstance(msg, AIMessage) and msg.content:
            ai_messages[msg.content] = True

    for msg in new_messages:
        if isinstance(msg, AIMessage) and msg.content:
            if msg.content not in ai_messages:
                msg.name = node_name
                new_state["messages"].append(msg)
                ai_messages[msg.content] = True
        else:
            msg.name = node_name
            new_state["messages"].append(msg)
            ai_messages[msg.content] = True

    new_state["template_id"] = ""
    new_state["template_message"] = ""
    new_state["negative_template_message"] = ""
    new_state["is_templated_anwser"] = False

    return new_state



def action_node(state: AgentState):
    return generic_node(state, "action_node", action_graph)

def general_node(state: AgentState):
    return generic_node(state, "general_node", general_graph)



builder = StateGraph(AgentState)
builder.add_edge(START, "supervisor")
builder.add_node("supervisor", supervisor_node)
builder.add_node("action_node", action_node)
builder.add_node("general_node", general_node)

graph = builder.compile(checkpointer=memory)