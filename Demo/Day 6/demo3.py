import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv('.env.local')
api_key=os.getenv("API_KEY")
llm=ChatGroq(model='openai/gpt-oss-120b',api_key=api_key)
user_prompt=input("Search Something..")
if user_prompt:
    result=llm.stream(user_prompt)

for chunk in result:
    print(chunk.content,end="")