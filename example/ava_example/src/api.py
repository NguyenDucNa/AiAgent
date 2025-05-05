from typing import Dict, Optional, List, Any
import json
import time
import logging
from contextlib import asynccontextmanager
from fastapi import (
    FastAPI,
    Request,
    Depends,
    Header,
    BackgroundTasks,
    Query,
)
from pydantic import BaseModel
from langfuse.callback import CallbackHandler
from sse_starlette.sse import EventSourceResponse
from fastapi.middleware.cors import CORSMiddleware
from langgraph.types import Command
from src.agent.supervisor import graph
from src.config import settings
from misa_logging import LogstashHandler, logstash_default, logger as elk_log

config = settings.ELK_CONF["handlers"]
err_handler = LogstashHandler(**config["logstash_error"])
biz_handler = LogstashHandler(**config["logstash_business"])
elk_log.add(biz_handler, **logstash_default)
elk_log.add(err_handler, **logstash_default)

logger = logging.getLogger("uvicorn.error")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting the app ...")
    yield
    logger.warning("Shutting down the app ...")


app = FastAPI(root_path=settings.API_CONF["root_path"], lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health Check"])
@app.get("/healthz", tags=["Health Check"])
def get_heathz() -> Dict[str, str]:
    return {"status": "ok"}


class PayloadRequest(BaseModel):
    assistant_id: str = ""
    input: Dict[str, Any] = {
        "messages": [["user", "Tôi muốn biết doanh thu của công ty trong tháng này"]]
    }
    config: Dict[str, Any] = {
        "configurable": {
            "tenant_id": "dqiueqqqq",
            "env": "test",
            "app": "AITESTMISAJSC",
            "user_id": "8d331727-bc85-40cd-b168-9b5664a6d3e4",
            "user_name": "Nguyễn Văn A",
            "gender": "Nam",
            "x_birthdate": "08/08/1990",
            "response_markdown": True,
            "message_id": "",
            "version": 4,
            "law_id": "",
            "flow": 2,
            "user_interface": "MAKT",
            "x_chatbot_sessionid": "1234",
            "x_report_endpoint": "http://demoamisapp.misa.vn.local/APIS/ChatbotAPI/api/ava/report",
            "this_monday": "01/04/2025",
            "this_sunday": "07/04/2025",
            "current_time": "04/04/2025",
            "employee_code": "123456",
            "x_tenantname": "Công ty sản xuất và phân phối dược phẩm, hóa mỹ phẩm"
        },
        "recursion_limit": 15
    }
    stream_mode: str = "events"
    stream_subgraphs: bool = False
    multitask_strategy: str = "enqueue"


from langchain_core.load.serializable import Serializable


def parse_start_event(event):
    if isinstance(event, Serializable):
        return event.__dict__
    elif isinstance(event, dict):
        return {k: parse_start_event(v) for k, v in event.items()}
    elif isinstance(event, list):
        return [parse_start_event(item) for item in event]
    elif isinstance(event, tuple):
        return tuple(parse_start_event(item) for item in event)
    else:
        return event



from src.nodes.general_node import (
    system_prompt as general_system_prompt,
    tools as general_tools,
)
from src.nodes.action_nodes import (
    system_prompt as action_system_prompt,
    tools as action_tools,
)

from langchain_core.utils.function_calling import convert_to_openai_tool


def parse_tools(tools):
    return [convert_to_openai_tool(tool) for tool in tools]


agent_mapping = {
    "general_node": (general_system_prompt, parse_tools(general_tools)),
    "action_node": (action_system_prompt, parse_tools(action_tools)),
}

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Command):
            # Convert Command to a dictionary
            return obj.__dict__  # Or a custom dictionary representation
        return super().default(obj)

async def stream_from_agent(
    input,
    config,
    log_data,
):
    node_goto = config.get("configurable", {}).get("node_goto")
    if node_goto and node_goto in agent_mapping:
        system_prompt, tools = agent_mapping[node_goto]
        yield json.dumps(
            {
                "event": "ignore",
                "data": {"tools": tools, "system_prompt": system_prompt},
            }
        )

    t1 = time.time()
    events = []
    run_idx = 0
    async for event in graph.astream_events(
        input,
        config=config,
        version="v2",
    ):
        t = time.time() - t1
        event = parse_start_event(event)
        if isinstance(event, dict):
            if event.get("metadata", {}).get("langgraph_node", "") in [
                "supervisor",
                "tool_choice",
            ]:
                continue
        if event["event"] == "on_chat_model_start":
            log_data["runs"].append(
                {
                    "run": run_idx,
                    "start": t,
                }
            )
        elif event["event"] == "on_chat_model_stream":
            if not "ttft" in log_data["runs"][-1]:
                log_data["runs"][-1]["ttft"] = t
        elif event["event"] == "on_chat_model_end":
            log_data["runs"][-1]["stream"] = t - log_data["runs"][-1]["ttft"]
            log_data["runs"][-1]["end"] = t
            run_idx += 1

        events.append({"time": t, "event": event["event"]})
        yield json.dumps(event, ensure_ascii=False, cls=CustomJSONEncoder)
    log_data["events"] = events


@app.post(
    "/threads/{session_id}/runs/stream",
)
async def dispatch(
    session_id: str,
    request: Request,
    request_body: PayloadRequest,
    background_tasks: BackgroundTasks,
):
    """
    tương tự API langgraph của MISAJSC, tuy nhiên bổ sung thêm 1 event 'send_message'
    format của event này là: {"message": "text"}
    message cần trả về nguyên vẹn cho client
    """
    logger.info(f"Received request for session {session_id}:\n{request_body.__dict__}")
    input = request_body.input
    config = request_body.config

    # Thêm thread_id vào configurable
    if "configurable" in config:
        config["configurable"]["thread_id"] = session_id

    log_data = {
        "session_id": session_id,
        "input": input.copy(),
        "config": config.copy(),
        "runs": [],
    }
    langfuse_handler = CallbackHandler(
        secret_key=settings.LANGFUSE_CONF["secret_key"],
        public_key=settings.LANGFUSE_CONF["public_key"],
        host=settings.LANGFUSE_CONF["host"],
        trace_name=settings.LANGFUSE_CONF["trace_name"],
        enabled=True,
        session_id=session_id,
        user_id=config.get("configurable", {}).get("user_id", ""),
        version="1.0.0",
    )
    config["callbacks"] = [langfuse_handler]
    config["recursion_limit"] = 15

    return EventSourceResponse(
        stream_from_agent(input, config, log_data), media_type="text/plain"
    )


async def stream_from_gen_agent(input, config, log_data, gen_graph):
    t1 = time.time()
    events = []
    run_idx = 0
    async for event in gen_graph.astream_events(
        input,
        config=config,
        version="v2",
    ):
        t = time.time() - t1
        event = parse_start_event(event)
        if isinstance(event, dict):
            if event.get("metadata", {}).get("langgraph_node", "") == "supervisor":
                continue
        if event["event"] == "on_chat_model_start":
            log_data["runs"].append(
                {
                    "run": run_idx,
                    "start": t,
                }
            )
        elif event["event"] == "on_chat_model_stream":
            if not "ttft" in log_data["runs"][-1]:
                log_data["runs"][-1]["ttft"] = t
        elif event["event"] == "on_chat_model_end":
            log_data["runs"][-1]["stream"] = t - log_data["runs"][-1]["ttft"]
            log_data["runs"][-1]["end"] = t
            run_idx += 1

        events.append({"time": t, "event": event["event"]})
        yield json.dumps(event)
    log_data["events"] = events



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8564,
    )
