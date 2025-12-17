import streamlit as st
import requests
import json
from dotenv import load_dotenv

def chat_local():
    st.header("Local LLM Chat Bot")

    if "local_messages" not in st.session_state:
        st.session_state.local_messages = []

    load_dotenv()
    api_key = "dummy key"

    url = "http://10.186.172.93:1234/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    user_prompt = st.chat_input("Search...")

    if user_prompt:
        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": [{"role": "user", "content": user_prompt}]
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()

        st.session_state.local_messages.append(("user", user_prompt))
        st.session_state.local_messages.append(
            ("assistant", result["choices"][0]["message"]["content"])
        )

    for role, msg in st.session_state.local_messages:
        with st.chat_message("human" if role == "user" else "ai"):
            st.write(msg)
