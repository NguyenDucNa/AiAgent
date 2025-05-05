import json
import time
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import (
    SystemMessage,
    AIMessage, 
    ToolMessage
)
from src.agent.base import AgentState
from src.tools.constants import Gender, Honorific, RecipientAddress
from src.tools.utils.time_util import get_current_time
from src.nodes.utils import organize_prompt_messages, _get_model
from src.config import settings
        
def get_system_config(config):
    sys_config = {}
    configuration = config.get("configurable", {})
    sys_config["user_name"] = configuration.get("user_name", "")
    sys_config["gender"] = configuration.get("gender", "")
    sys_config["x_birthdate"] = configuration.get("x_birthdate", "")
    sys_config["current_time"] = configuration.get("current_time", get_current_time())
    sys_config["this_sunday"] = configuration.get("this_sunday", "")
    sys_config["this_monday"] = configuration.get("this_monday", "")
    sys_config["x_culture"] = configuration.get("x_culture", "vi")
    sys_config["x_tenantname"] = configuration.get("x_tenantname", "")
    return sys_config


class BaseNode:
    def __init__(self, model_config_key, system_prompt_template, tools, tool_choice=None):
        self.model = _get_model(settings.LLM_CONF[model_config_key], tools, tool_choice)
        self.system_prompt_template = system_prompt_template
        self.tool_node = ToolNode(tools)

    def should_continue(self, state):
        messages = state["messages"]
        last_message = messages[-1]
        print("last_message", last_message)
        if not last_message.tool_calls:
            return "end"
        else:
            return "continue"
        
    # def action_to_agent_condition(self, state):
    #     messages = state["messages"]
    #     last_message = messages[-1]
    #     if "function_calling" in last_message.content:
    #         return "end"
    #     else:
    #         return "continue"

    def action_to_agent_condition(self, state):
        last_message = state["messages"][-1]
        content = getattr(last_message, "content", {})

        if isinstance(content, dict) and "function_calling" in content:
            func_call = content["function_calling"]
            if func_call.get("name"):  # Nếu có name (không rỗng)
                return "end"
            else:
                return "continue"

        # Nếu không có function_calling thì cứ tiếp tục
        return "continue"


        
    def use_template(self, state, last_message, config):
        template_mapping = {}
        content = json.loads(last_message.content)
        content_message = content.get("message", "")
        content_data = content.get("data", [])
        # Số người sinh nhật
        gender = config["metadata"]["gender"]
        honorific = Honorific.MALE.value if gender == Gender.MALE.value else Honorific.FEMALE.value

        x_age = int(config["metadata"]["x_birthdate"].split("/")[2])
        
        template = state["template_message"]
        template_mapping.update({
            'honorific': honorific,
            'honorific_lower': honorific.lower(),
            'content_message': content_message
        })

        if len(content_data) == 0:
            template = state["negative_template_message"]
        else:
            # Trích xuất item_template từ temp
            start_marker = ':$$'
            end_marker = '$$'
            start_index = template.find(start_marker) + len(start_marker)
            end_index = template.find(end_marker, start_index)
            item_template = template[start_index:end_index].strip()

            template = template.replace(f"{start_marker}{item_template}{end_marker}", "")

            template_mapping.update({
                'Number_Of_People': len(content_data)
            })
            content_data_list = "\n"
            item_template += "\n"
            for i, item in enumerate(content_data):
                if i==0 and 'Birthday' in last_message.name:
                    recipient_address = "" 
                    age_diff = x_age - int(item["date_of_birth"].split("/")[2])
                    if  age_diff > 0:
                        recipient_address = RecipientAddress.MALE.value if item["gender"] == Gender.MALE.value else RecipientAddress.FEMALE.value
                    elif age_diff == 0:
                        recipient_address = RecipientAddress.FRIEND.value
                    else:
                        recipient_address  = RecipientAddress.YOUNGER.value
                    template_mapping.update({
                        'recipient_address': recipient_address,
                        'recipient_firstname': item["person_name"],
                        'fist_birthday_wish': item.get("birthday_wish", "")
                    })

                content_data_list += item_template.format(**item)

            template_mapping.update({
                'ContentDataList': content_data_list
            })

        template_content = template.format(**template_mapping)        
        kwargs = {
            "id": f"run-template-{last_message.name}-{int(time.time() * 1000)}",
            "name": None,
            "type": "ai",
            "example": False,
            "tool_calls": [
            ],
            "usage_metadata": {
                "input_tokens": 0,
                "total_tokens": 0,
                "output_tokens": 0,
                "input_token_details": {
                    "audio": 0,
                    "cache_read": 0
                },
                "output_token_details": {
                    "audio": 0,
                    "reasoning": 0
                }
            },
            "additional_kwargs": {
            },
            "response_metadata": {
                "model_name": "gpt-4o-2024-08-06",
                "finish_reason": "stop",
                "system_fingerprint": "fp_eb9dce56a8"
            },
            "invalid_tool_calls": [
            ]
        }
        ai_message = AIMessage(content=template_content, **kwargs)
        state["messages"].append(ai_message)
        state["cache_audit"] = 2
        return state 


    def call_model(self, state: AgentState, config: RunnableConfig):
        last_message = state["messages"][-1]
        if isinstance(last_message, AIMessage) and last_message.tool_calls:
            return state
        
        if isinstance(last_message, ToolMessage) and state.get("template_id") and state.get("is_templated_anwser"):
            state = self.use_template(state, last_message, config)

        sys_config = get_system_config(config)

        new_state = organize_prompt_messages(state)
        messages = new_state["messages"]
        prompt = self.system_prompt_template.format(**sys_config)
        messages = [SystemMessage(prompt)] + messages

        response = self.model.invoke(messages)
        if response.tool_calls:
            dedup_tool_calls = []
            tool_name = {}
            for tool_call in reversed(response.tool_calls):
                _key = tool_call["name"] + str(tool_call['args'])
                if _key not in tool_name:
                    tool_name[_key] = True
                    dedup_tool_calls.append(tool_call)
            response.tool_calls = dedup_tool_calls
        return {"messages": [response]}
