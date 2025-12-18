import os
import requests
import streamlit as st
import json
import time
from dotenv import load_dotenv

st.header("Local LLM Chat Bot")

# Load environment variables (if any)
load_dotenv()
api_key = "dummy-key"  # replace with os.getenv("API_KEY") in production

# API setup
url = "http://10.186.172.93:1234/v1/chat/completions"
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Chat input
user_prompt = st.chat_input("Enter something...")

# Only send request if user entered something
if user_prompt:
    req_data = {
        'model': 'openai/gpt-oss-20b',
        'messages': [
            {
                'role': 'user',
                'content': user_prompt
            }
        ],
    }

    # Make API request
    time1=time.perf_counter()
    response = requests.post(url, data=json.dumps(req_data), headers=headers)
    time2=time.perf_counter()
    timereq=time2-time1
    # Check response
    if response.status_code == 200:
        res = response.json()
        if "choices" in res and len(res["choices"]) > 0:
            st.write(res["choices"][0]["message"]["content"])
            st.write(timereq) 
        else:
            st.error("No response from the API")
    else:
        st.error(f"API Error {response.status_code}: {response.text}")
