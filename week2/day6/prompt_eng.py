import os
from  pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kha hai bhai")

client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"


def llm_ans(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    return ans


bad_prompt="""
#ROLE:
You are a support assistant at a mobile/laptop company
#TASK
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue in one of these categories namely billing,technical,return
#OUTPUT FORMAT
Your answer should be in one word only.The one word should be one of the categories given in constrainsts.
#Example
For instance if a user says he wants a refund then the category is Return
#FALLBACK
If the issue is unreleated to any of the categories mentioned in constrainsts, then the answer should be OTHER
This is a user complaint:
My laptop is not working


"""

print(llm_ans(bad_prompt))