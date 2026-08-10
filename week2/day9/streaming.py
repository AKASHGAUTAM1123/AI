import os
from pathlib import Path
from time import sleep
from dotenv import load_dotenv
from groq import Groq
import re

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
prompt="Expalin how internet works."
message={

    "role": "user",
    "content" : prompt
}
messages=[message]
# reponse1=client.chat.completions.create(model=model, messages=messages)
# answer=reponse1.choices[0].message.content
# print(answer)


stream=client.chat.completions.create(model=model,messages=messages,stream=True)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="",flush=True)