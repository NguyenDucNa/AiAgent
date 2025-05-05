import json
import time
from typing import Literal
from typing_extensions import TypedDict

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from src.tools import chat
from src.nodes.base import get_system_config
from openai import OpenAI
from src.ai_core.constants import (
    subgraph_mapping,
    router_agent_prompt,
    tool_choice_prompt,
)
from src.agent.base import AgentState
from src.config import settings

base_url = settings.LLM_CONF["openai"]["base_url"]
api_key = settings.LLM_CONF["openai"]["api_key"]
model = settings.LLM_CONF["openai"]["model"]

llm_tool_choice = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model=model,
    temperature=0,
    # max_tokens=10,
    stream_usage=True,
)


llm_router_agent = ChatOpenAI(
    base_url=settings.LLM_CONF["openai"]["base_url"],
    api_key=settings.LLM_CONF["openai"]["api_key"],
    model=settings.LLM_CONF["openai"]["model"],
    temperature=0,
    stream_usage=True,
)


def tools_to_schema(tools: list):
    schemas = []
    for t in tools:
        schema = {
                "name": t.name,
                "description": t.description,
                "parameters": t.args_schema.model_json_schema()
            }
        # for k, v in schema["parameters"]["properties"].items():
        #     if "anyOf" in v:
        #         v.update(v["anyOf"][0])
        #         v.pop("anyOf", None)
        schema["parameters"]["properties"].pop("state", None)
        if "required" in schema["parameters"]:
            schema["parameters"]["required"] = [
                key for key in schema["parameters"]["required"] if key != "state"
            ]
        schemas.append(
            {
            "type": "function",
            "function": schema
        }
        )
    return schemas

def tool_choice(
    state: AgentState, tools: list, next_agent: str, config: RunnableConfig
) -> str:
    fake_tools = []
    try:
        start_time = time.time()
        tools.insert(0, chat)
        tool_list = tools_to_schema(tools)
        sys_config = get_system_config(config)
        
        messages = []
        for msg in state["messages"][-6:]:
            if isinstance(msg, AIMessage):
                if msg.tool_calls:
                    _name = [t["name"] for t in msg.tool_calls]
                    content = f"Using tools: {', '.join(_name)}"
                    messages.append(f"assistant: {content}")
                else:
                    messages.append(f"assistant: {msg.content}")
            elif isinstance(msg, HumanMessage):
                messages.append(f"user: {msg.content}")
            elif isinstance(msg, ToolMessage):
                messages.append(f"Tool data: {msg.content}")
                
        prompt = tool_choice_prompt.format(**sys_config, chat_history="\n".join(messages)).strip()
        res = llm_tool_choice.invoke(
            [
                (
                    "human",
                    prompt,
                ),
            ],
            tools=tool_list,
            tool_choice="required"
        )
        if res.tool_calls and res.tool_calls[0] == "chat":
            return fake_tools
        res.name = next_agent
        end_time = time.time() - start_time
        print("Tool choice: ", end_time)
        return [res]
    except Exception as e:
        print(e)
        return fake_tools


class NextAgent(TypedDict):
    agent: Literal["A0", "A1", "A2"]

def router_agent(state: AgentState) -> str:
    messages = []
    for msg in state["messages"]:
        if isinstance(msg, AIMessage) and msg.content:
            messages.append(f"assistant: {msg.content}")
        elif isinstance(msg, HumanMessage):
            messages.append(f"user: {msg.content}")

    new_messages = [
        (
            "human",
            router_agent_prompt.format(chat_history="\n".join(messages[-4:])),
        ),
    ]
    response = llm_router_agent.with_structured_output(NextAgent).invoke(new_messages)
    try:
        next_agent = response.get("agent", "A0").upper()
        goto = subgraph_mapping[next_agent]
    except:
        goto = subgraph_mapping["A0"]
    return goto
