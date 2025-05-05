import requests
from src.config import settings

def get_suggestion_message(
    user_id: str = "",
    tenant_id: str = "",
    assistant_code: str = "",
    tool_name: str = "",
    language: str = "vi",
) -> str:
    """ Lấy mẫu câu trả lời """
    url_api = f'{settings.AVA_CORE_CONF["base_url"]}/Suggestions?userId={user_id}&tool={tool_name}&language={language}'
    if tenant_id:
        url_api +=f"&tenantId={tenant_id}"
    if assistant_code:
        url_api+=f"&assistantCode={assistant_code}"

    headers = {}
    if settings.AVA_CORE_CONF["x_misa_api_key"]:
        headers.update({'x-misa-api-key': settings.AVA_CORE_CONF["x_misa_api_key"]})
    response = requests.get(url_api, headers=headers)
    if response.status_code == 200:
        return response.json().get("TemplateAnswer", None)
    else:
        return None
    
def create_suggestion_message(
    user_id: str = "",
    tenant_id: str = "",
    assistant_code: str = "",
    tool_name: str = "",
    message: str = "",
    template: str = "",
    language: str = "vi",
):
    """ Tạo mẫu câu trả lời """
    json_data = {
        "userId": user_id,
        "tenantId": tenant_id,
        "assistantCode": assistant_code,
        "tool": tool_name,
        "language": language,
        "message": message,
        "templateAnswer": template,
    }
    url_api = f'{settings.AVA_CORE_CONF["base_url"]}/Suggestions'
    headers = {
        'Content-Type': 'application/json'
    }
    if settings.AVA_CORE_CONF["x_misa_api_key"]:
        headers.update({'x-misa-api-key': settings.AVA_CORE_CONF["x_misa_api_key"]})
    response = requests.post(url_api, headers=headers, json=json_data)
    if response.status_code == 200:
        return True
    else:
        return False



