import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kha hai bhai")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"


# Step 1: Knowledge Base
knowledge_base = {
    "about": "Akash is a Good Boy",
    "age": "The age of Akash is 20 years",
    "net worth": "The net worth of Akash is 2000"
}


# Step 2: Retrieval
def retrieve_info(question):
    question = question.lower()

    if "net worth" in question:
        return knowledge_base["net worth"]

    elif "age" in question:
        return knowledge_base["age"]

    elif "about" in question or "who is" in question or "akash" in question:
        return knowledge_base["about"]

    else:
        return None


# Step 3: Generate Answer using LLM
def ask_llm(question):

    # Retrieve relevant information
    context = retrieve_info(question)

    sys_prompt = f"""
Answer in one line only.

Answer only based on the given context.
Do not hallucinate.
If the answer is not available in the context, say:
"I don't have enough information."

Context:
{context}
"""

    system_message = {
        "role": "system",
        "content": sys_prompt
    }

    user_message = {
        "role": "user",
        "content": question
    }

    messages = [system_message, user_message]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    answer = response.choices[0].message.content

    return answer


# Step 4: Ask Question
question = "What is Akash's net worth?"

print(ask_llm(question))