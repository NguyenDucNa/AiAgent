import requests
import time
import json

def call_api(
    url: str,
    session_id: str,
    data: dict
):
    headers = {
        "Content-Type": "application/json",
        "x-chatbot-sessionid": session_id
    }
    data = json.dumps(data, ensure_ascii=False)

    st = time.time()
    response = requests.post(url, headers=headers, data=data)
    et = time.time()

    log = {
        "duration": et - st,
        "inputs": {
            "url": url,
            "headers": headers,
            "data": data
        },
        "outputs": {
            "status_code": response.status_code,
            "body": response.text
        }
    }
    print("=====================================", flush=True)
    print("API CALL LOG:" + json.dumps(log, indent=4), flush=True)
    print("=====================================", flush=True)
    return response.status_code, response.text, log