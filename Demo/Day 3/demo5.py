import os
import requests
import json
from dotenv import load_dotenv
load_dotenv(".env.local")
api_key=os.getenv("API_KEY")
url="https://api.groq.com/openai/v1/chat/completions"
headers={
    "Authorization":f"Bearer {api_key}",
    "Content-Type":"application/json"
}
user_prompt=input("Search..")

req={
    "model":"llama-3.3-70b-versatile",
    "messages":[
        {"role":"user","content":user_prompt}
    ],
}
response=requests.post(url,data=json.dumps(req),headers=headers)
print("Status",response.status_code)
print(response.json())