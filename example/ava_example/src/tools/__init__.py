import os
import sys
project_root = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../../../../.."))
sys.path.append(project_root)

from src.tools.action import action_tools
from src.tools.general import general_tools    
from langchain_core.tools import tool


tool_mapping = {
    "general_tools": general_tools,
    "action_node": action_tools,
}

def get_unique_tools(tools_list):
    unique_tools = []
    unique_ids = []
    
    for tool in tools_list:
        if id(tool) not in unique_ids:
            unique_ids.append(id(tool))
            unique_tools.append(tool)
    
    return unique_tools

@tool
def chat() -> str:
    """
    - Sử dụng tool này để đưa ra câu trả lời cho user khi không cần tra cứu thông tin bên ngoài.
    - Sử dụng khi đã có đủ thông tin để trả lời user.
    - Sử dụng tool này khi không có tool nào phù hợp để xử lý tin nhắn của user."""
    pass

# Assuming tools is your combined list
tools = general_tools + action_tools
tools = get_unique_tools(tools)
# tools = [general_tools[0]]
