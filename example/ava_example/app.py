import streamlit as st
st.set_page_config(layout="wide", page_title="MAKT")
import time
import yaml
import asyncio
from uuid import uuid4
from streamlit import runtime
from pymongo import MongoClient
from typing import AsyncGenerator
from langfuse.callback import CallbackHandler
from datetime import datetime, timezone, timedelta
from streamlit.runtime.scriptrunner import get_script_run_ctx
from src.tools.utils.time_util import get_current_time, get_this_week_time

from src.agent.supervisor import graph

@st.cache_resource
def connect_mongo():
    client = MongoClient(
        "mongodb://10.0.6.92:27017/?directConnection=true",
        username=None,
        password=None,
        connect=False,
    )
    return client["MISAJSC-Langgraph"]

mongo_db = connect_mongo()

def get_remote_ip() -> str:
    try:
        ctx = get_script_run_ctx()
        if ctx is None:
            return None
        session_info = runtime.get_instance().get_client(ctx.session_id)
        if session_info is None:
            return None
    except Exception as e:
        return None
    return session_info.request.remote_ip

def init(data):
    session_id = str(uuid4())
    st.session_state.session_id = session_id
    langfuse_handler = CallbackHandler(
        secret_key="sk-lf-edaea6b6-798c-4cdf-8c72-c15ddf8ad7b6",
        public_key="pk-lf-866ab41c-bf15-48b8-a072-2dd3f165aaa7",
        host="http://10.0.6.135:3000",
        trace_name="AVA_MXH",
        enabled=True,
        session_id=session_id,
        user_id=data.get("user_id", ""),
        version="1.0.0"
    )
    data["thread_id"] = session_id
    print(data)
    st.session_state.config = {"configurable": data, "callbacks": [langfuse_handler], "recursion_limit": 15}

st.title("Chat with MAKT")
st.button("Clear message", on_click=lambda: st.session_state.clear())

with st.expander("Config", expanded = False):
    col1, col2, col3, col4 = st.columns(4)
    user_name = col1.text_input("User Name", key="user_name", value="Nguyễn Ngoc Anh")
    gender = col2.text_input("Gender", key="gender", value="Nam")
    user_dob = col3.text_input("User Date-of-Birth", key="user_dob", value="08/08/1990")
    user_id = col4.text_input("User ID", key="user_id", value="05484619-0cee-4998-94f1-a4228cd430af")

    col5, col6, col7, col8 = st.columns(4)
    x_tenantname = col5.text_input("X-TenantName", key="x_tenantname", value="Công ty cổ phần MISA")
    user_interface = col6.text_input("Đang ở giao diện(MXH or MAKT)", key="user_interface", value="MXH")

    # col7, col8, col9 = st.columns(3)
    x_sessionid = col7.text_input("X-SessionID", key="x_sessionid", value="32131")
    # x_report_endpoint = col8.text_input("X-Report Endpoint", key="x_report_endpoint", value="http://demoamisapp.misa.vn.local/APIS/ChatbotAPI/api/ava/report")
    phone_number = col8.text_input("Số điện thoại", key="phone_number", value="0987654321")
   
    current_time = get_current_time()
    week_time = get_this_week_time()
    this_monday = week_time["monday"]
    this_sunday = week_time["sunday"]
    # current_time = current_time.replace("2025", "2024")

    submit = st.button("Submit")
    if submit:
        data = {
            'tenant_id': "dqiueqqqq",
            'tenant_id': "dqiueqqqq",
            'env': 'test',
            'app': 'AITESTMISAJSC',
            'user_id': user_id,
            'user_name': user_name,
            'gender': gender,
            'x_birthdate': user_dob,
            'response_markdown': True,
            'message_id': '',
            'version': 4,
            'law_id': '',
            'flow': 2,
            'user_interface': user_interface,
            'x_chatbot_sessionid': x_sessionid,
            'x_report_endpoint': "https://",
            'this_monday': this_monday,
            'this_sunday': this_sunday,
            'current_time': current_time,
            'employee_code': '123456',
            'x_tenantname': x_tenantname,
            'phone_number': phone_number,
        }
        init(data)

if "config" not in st.session_state:
    init({})

if "messages" not in st.session_state:
    st.session_state.messages = []

if "tool_info" not in st.session_state:
    st.session_state.tool_info = {}

class ResponseInfo:
    def __init__(self):
        self.content = ""
        self.tool_execution_details = ""
        self.tool_results = ""
        self.tool_name = ""
        self.bot_name = ""
        
async def process_events():
    if not st.session_state.config["configurable"].get("x_chatbot_sessionid"):
        st.write("Bạn cần nhập X-Chatbot-SessionID trong Config")
        return 
    
    # Tạo ID cho phản hồi này
    response_id = uuid4().hex
    response_info = ResponseInfo()
    
    start_time = time.time()
    async for event in graph.astream_events(inputs, config=st.session_state.config, version="v2"):
        kind = event["event"]
        
        
        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content:
                response_info.content += content
                response_info.content += content
                yield content
            
            usage_metadata = event["data"]["chunk"].usage_metadata
            if usage_metadata:
                print(event)
                input_tokens = usage_metadata["input_tokens"]
                output_tokens = usage_metadata["output_tokens"]
                if "gpt-4o-2024-08-06" in event["metadata"]["ls_model_name"]:
                    price = ((input_tokens/1000000)*2.5) + ((output_tokens/1000000)*10)
                else:
                    price = ((input_tokens/1000000)*0.15) + ((output_tokens/1000000)*0.6)                
                usage = f"**{input_tokens} input token và {output_tokens} output token.**\n\n**Giá: {round(price, 6)}$ ~ {round(price*24860.00, 2)} VND**"
                print("\n\n=======================\n\n" + usage)
                
                
                bot_name = event["metadata"]["checkpoint_ns"].split(":")[0]
                response_info.bot_name = bot_name
                yield f"\n\n**Response by {bot_name}**\n\n"
                
        elif kind == "on_tool_start":
            content = f"Tool usage: {event['name']} with inputs: {event['data'].get('input')}"
            response_info.tool_execution_details += "\n\n" + content + "\n\n"
            response_info.tool_name = event['name']
            
        elif kind == "on_tool_end":
            print(f"Done tool: {event['name']}")
            
            # Lấy kết quả của Tool
            if 'data' in event and 'output' in event['data']:
                tool_output = event['data']['output']
                
                # Kiểm tra nếu output là ToolMessage hoặc object có attribute content
                if hasattr(tool_output, 'content'):
                    tool_content = tool_output.content
                    
                    # Thử parse nếu là JSON
                    try:
                        import json
                        json_content = json.loads(tool_content)
                        formatted_content = json.dumps(json_content, indent=2, ensure_ascii=False)
                        tool_output_content = f"```json\n{formatted_content}\n```"
                    except:
                        tool_output_content = f"```\n{tool_content}\n```"
                else:
                    # Nếu không có attribute content, convert sang string
                    tool_output_content = f"```\n{str(tool_output)}\n```"
                
                response_info.tool_results += f"\n\n**Tool Result ({event['name']}):**\n{tool_output_content}\n\n"
            
            print(f"Tool output was: {event}")
            print("--")
        elif kind == "on_custom_event":
            if "message" in event["data"]:
                content = event["data"]["message"]
                yield content
            else:
                tool_content = event["data"]["function_info"]
                try:
                    import json
                    json_content = json.loads(tool_content)
                    formatted_content = json.dumps(json_content, indent=2, ensure_ascii=False)
                    tool_output_content = f"```json\n{formatted_content}\n```"
                except:
                    tool_output_content = f"```\n{tool_content}\n```"
                tool_results = f"\n\n**Tool Result ({event['name']}):**\n{tool_output_content}\n\n"
                st.session_state.tool_info[response_id] = {
                    "execution_details": event["data"]["function_info"],
                    "results": tool_results,
                    "name": event["name"]
                }

        # Lưu thông tin tool vào session state với ID phản hồi
        if response_info.tool_execution_details or response_info.tool_results:
            st.session_state.tool_info[response_id] = {
                "execution_details": response_info.tool_execution_details.strip() if response_info.tool_execution_details else None,
                "results": response_info.tool_results.strip() if response_info.tool_results else None,
                "name": response_info.tool_name
            }
        
        # Lưu ID cho phần hiển thị expander
        st.session_state["current_response_id"] = response_id

def to_sync_generator(async_gen: AsyncGenerator):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        while True:
            try:
                yield loop.run_until_complete(anext(async_gen))
            except StopAsyncIteration:
                break
    finally:
        loop.close()

# Hiển thị lịch sử trò chuyện
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)
        
        # Hiển thị thông tin tool cho phản hồi cũ nếu có
        if message["role"] == "assistant" and "id" in message and message["id"] in st.session_state.tool_info:
            tool_info = st.session_state.tool_info[message["id"]]
            if tool_info["execution_details"] or tool_info["results"]:
                with st.expander("🛠️ Tool Information", expanded=False):
                    if tool_info["execution_details"]:
                        st.markdown("### 🔍 Tool Execution Details")
                        st.markdown(tool_info["execution_details"])
                    if tool_info["results"]:
                        st.markdown("### 📊 Tool Results")
                        st.markdown(tool_info["results"])
        

if prompt := st.chat_input("What is up?", max_chars=1000):
    if not st.session_state["messages"]:
        mongo_db["conversations"].insert_one({
            "session_id": st.session_state["session_id"],
            "messages": [],
            "created_at": datetime.now().astimezone(timezone(timedelta(hours = 7))).isoformat()
        })
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        inputs = {"messages": [("user", prompt)]}
        start_time = time.time()
        response = st.write_stream(to_sync_generator(process_events()))
        end_time = time.time() - start_time
        st.write(f"**Total time process**: {end_time}")
        
        # Hiển thị thông tin tool trong expander
        if "current_response_id" in st.session_state and st.session_state["current_response_id"] in st.session_state.tool_info:
            response_id = st.session_state["current_response_id"]
            tool_info = st.session_state.tool_info[response_id]
            if tool_info["execution_details"] or tool_info["results"]:
                with st.expander("🛠️ Tool Information", expanded=False):
                    if tool_info["execution_details"]:
                        st.markdown("### 🔍 Tool Execution Details")
                        st.markdown(tool_info["execution_details"])
                    if tool_info["results"]:
                        st.markdown("### 📊 Tool Results")
                        st.markdown(tool_info["results"])
        
        id = uuid4().hex
        if "current_response_id" in st.session_state:
            # Gán ID phản hồi cho ID công cụ đã lưu
            id = st.session_state["current_response_id"]
            # Xóa ID tạm thời
            del st.session_state["current_response_id"]
        
        st.session_state.messages.append({"role": "assistant", "content": response, "id": id, "stars": 0})
        mongo_db["conversations"].update_one(
            {
                "session_id": st.session_state["session_id"]
            },
            {
                "$push": {
                    "messages": {
                        "message_id": id,
                        "user": prompt,
                        "assistant": response,
                        "stars": 0,
                        "feedback_message": "",
                        "created_at": datetime.now().astimezone(timezone(timedelta(hours = 7))).isoformat()
                    }
                }
            }
        )
