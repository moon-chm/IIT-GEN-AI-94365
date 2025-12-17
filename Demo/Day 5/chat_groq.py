import os
import requests
import streamlit as st
from dotenv import load_dotenv

def chat_groq():
    st.header("Groq Chat Bot")

    if "groq_messages" not in st.session_state:
        st.session_state.groq_messages = []

    load_dotenv(".env.local")
    api_key = os.getenv("API_KEY")

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    user_prompt = st.chat_input("Enter something")

    if user_prompt:
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": user_prompt}]
        }

        response = requests.post(url, headers=headers, json=payload)
        result = response.json()

        st.session_state.groq_messages.append(("user", user_prompt))
        st.session_state.groq_messages.append(
            ("assistant", result["choices"][0]["message"]["content"])
        )

    for role, msg in st.session_state.groq_messages:
        with st.chat_message("human" if role == "user" else "ai"):
            st.write(msg)
