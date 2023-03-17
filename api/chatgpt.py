from api.prompt import Prompt

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatGPT:
    def __init__(self):
       # self.prompt = Prompt()
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-3.5-turbo")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 240))
  
    
    def get_response(self):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
           # {"role": "system", "content": "你是說中文繁體中文的專家"},
           # {"role": "assistant", "content": "你是說中文繁體中文的 rexx 語言專家"},
           # {"role": "user", "content": input("You: ")}
            {"role": "user", "content": self.prompt}
        ]
        )
        return response['choices'][0].message.content

    def add_msg(self, text):
        self.prompt=text
