import re
import json
import base64
import time

from typing import List, Dict, Text
from openai import OpenAI as AOI
from openai import RateLimitError, AuthenticationError, APIError

from src.config import settings
from src.tools.utils.prompt_template import IMAGE_EXTRACT_PROMPT, SUGGEST_SOLUTIONS_PROMPT, PROMPT_TEMPLATE

class OpenAIGenerator():
    
    def __init__(self) -> None:
        """
         Initialize OpenAI.
        """
        
        self.client = AOI(
            base_url = settings.LLM_CONF["openai"]["base_url"],
            api_key = settings.LLM_CONF["openai"]["api_key"],
            # log_config = settings.OPENAI_CONF["log_config"]
        )
        self.model = settings.LLM_CONF["openai"]["model"]

    def extract_text_from_image(self, image_data: bytes):
        data = base64.b64encode(image_data).decode("utf-8")
        result = self.client.chat.completions.create(
            messages = [
                {
                    "role": "user",
                    "content": [
                        IMAGE_EXTRACT_PROMPT,
                        {"image": data, "resize": 768}
                    ]
                }, 
            ],
            model = "gpt-4o-mini",
            temperature = 0.0,
            max_tokens = 500,
            response_format = {
                "type": "json_schema",
                "json_schema": {
                    "name": "extracted_text",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string"}
                        },
                        "required": ["text"],
                        "additionalProperties": False
                    },
                    "strict": True
                },
            }
        )
        content = result.choices[0].message.content
        extracted_text = json.loads(content)["text"]
        # logger.debug(f"Extracted text from image: {extracted_text}")
        return extracted_text
    
    def suggest_solutions(
        self,
        error_text: str
    ):
        result = self.client.chat.completions.create(
            messages = [
                {
                    "role": "system",
                    "content": SUGGEST_SOLUTIONS_PROMPT
                },
                {
                    "role": "user",
                    "content": f"Thông báo lỗi từ phần mềm: {error_text}"
                }, 
            ],
            model = "gpt-4o",
            temperature = 0.0,
            max_tokens = 500,
        )
        content = result.choices[0].message.content
        # logger.debug(f"Suggest solutions: {content}")
        return content
    
    def call_openai(self, messages: List[Dict[Text, Text]], max_tokens = None, **kwargs):
        """
         Send messages to OpenAI and return response. This is a blocking call and will wait for API response or API error

         Args:
                 messages: List of messages to send
        """
        # logger.debug(f"Send messsage to OpenAI:{messages}")
        # OpenAI API key is used to get the current key and create a new chat completion.
        try:
            res = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                # max_tokens=max_tokens,
                timeout=60,
                **kwargs)
            return res
        except (RateLimitError, AuthenticationError, APIError) as e1:
            msg = f"OpenAI key has below problem\n{e1}"
            # logger.warning(msg)
        except Exception as e3:
            # logger.warning(
            #     f"OpenAI model has below problem\n{e3}")
            pass

    @staticmethod
    def get_usage(res):
        return {
            "completion_tokens": res.usage.completion_tokens,
            "prompt_tokens": res.usage.prompt_tokens,
            "total_tokens": res.usage.total_tokens,
        }
    
    def capitalize_after_punctuation(self, text):
        # Define a regular expression pattern to match words following punctuation
        pattern = r'(?<=[.!?])\s*\w'
        
        # Define a function to capitalize the matched word
        def capitalize(match):
            return match.group().upper()
        
        # Use the re.sub() function to replace the matched words with their uppercase versions
        result = re.sub(pattern, capitalize, text)
    
        return result

    def clean_answer(self, answer: Text):
        if "](" in answer:
            answer = answer.replace("[link](", "")
            answer = answer.replace("](", ": ")
            answer = answer.replace(" [", " ")
            answer = answer.replace(")", "")
        # if "Câu trả lời:" in answer:
        #     answer = answer.split("Câu trả lời:")[-1]
        # if "Trả lời:" in answer:
        #     answer = answer.split("Trả lời:")[-1]
        # if "Answer:" in answer:
        #     answer = answer.split("Answer:")[-1]
        # if "phản hồi:" in answer:
        #     answer = answer.split("phản hồi:")[-1]
        # if "Phản hồi:" in answer:
        #     answer = answer.split("Phản hồi:")[-1]
        sentences = answer.split(". ")
        sentences = [sentence for sentence in sentences if "http" not in sentence]
        answer = ". ".join(sentences)
        answer = answer.replace("quý khách", "Quý khách")
        if answer.startswith("Quý khách"):
            answer = answer.replace("Quý khách ", "", 1)
            answer = answer[0].upper() + answer[1:]
        answer = self.capitalize_after_punctuation(answer)
        return answer.strip()
    
    def get_answer(
        self,
        question: Text,
        doc: Text,
    ):
        """
         Get answer to a question.

         Args:
            :param question: User question
            :param candidates: list of documents relevant to this question
            :param stream: if False return answer as string
        """
        messages = []

        doc_str = "<knowledge>\n" + doc + "\n</knowledge>"
        # logger.debug(f"Related docs for question: {question}\n")
        prompt_content = PROMPT_TEMPLATE.format(
            context=doc_str)
        
        messages.append({"role": "system", "content": prompt_content})
        messages.append({"role": "user", "content": question})

        start_time = time.time()
        res = self.call_openai(
            messages=messages,
            temperature=settings.LLM_CONF["openai"]["temperature"]
        )
        
        answer = ""
        usage = {}
        if res.choices:
            answer = res.choices[0].message.content
            answer = self.clean_answer(answer)
            usage = self.get_usage(res)
        time_use = time.time() - start_time
        usage["time"] = time_use
        # logger.debug("---Generate Answer use OpenAI: %s seconds ---" %
        #                 (time_use))
        return answer, usage