import time
import json
from functools import lru_cache
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    trim_messages
)
from langgraph.prebuilt.chat_agent_executor import AgentState

def organize_prompt_messages(state: AgentState, max_tokens: int = 15, model: str = "gpt-4o") -> AgentState:
    new_state = state.copy()
    new_state["messages"] = trim_messages(
        new_state["messages"],
        max_tokens=max_tokens,
        strategy="last",
        token_counter=len,
        include_system=False,
        allow_partial=True,
        start_on="human",
    )
    return new_state

def _get_model(config: dict, tools: list, tool_choice):
    base_url = config["base_url"]
    api_key = config["api_key"]
    model = ChatOpenAI(base_url=base_url, api_key=api_key, model=config["model"], temperature=config["temperature"], stream_usage=True)

    model = model.bind_tools(tools, tool_choice=tool_choice)
    return model