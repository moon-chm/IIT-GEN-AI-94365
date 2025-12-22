from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
import os
from dotenv import load_dotenv
import json
import requests
import streamlit as st

st.header("Chat Agent")

@tool
def weather(city):
    load_dotenv('.env.local')
    try:
        api_key = os.getenv("weather")
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
        response = requests.get(url)
        weather = response.json()
        return json.dumps(weather)
    except:
        return "Error"

@tool
def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error"

@tool
def read_file(filename: str) -> str:
    try:
        if not os.path.exists(filename):
            return f'error: File {filename} not found.'
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except Exception as e:
        return f"error reading file: {str(e)}"

llm = init_chat_model(
    model='google/gemma-3-4b',
    model_provider='openai',
    base_url='http://127.0.0.1:1234/v1',
    api_key='none'
)

agent = create_agent(
    model=llm,
    tools=[weather, calculator, read_file],
    system_prompt="You are an expert short answer assistant"
)

# Conversation history
if 'convo' not in st.session_state:
    st.session_state.convo = []

# Chat input
user_prompt = st.chat_input("Search Something: ")
file_taker = st.file_uploader("Upload file", type=['csv', 'txt', 'pdf'])

# Handle user text
if user_prompt:
    st.session_state.convo.append({
        'role': 'user',
        'content': user_prompt
    })
    result = agent.invoke({'messages': st.session_state.convo})
    ai_msg = result['messages'][-1]
    st.write(user_prompt)
    st.write(ai_msg.content)
    st.session_state.convo = result['messages']

# Handle uploaded file
if file_taker:
    try:
        file_content = file_taker.read().decode("utf-8")
    except:
        file_content = f"Could not read file {file_taker.name}"

    st.session_state.convo.append({
        'role': 'user',
        'content': file_content
    })

    result = agent.invoke({'messages': st.session_state.convo})
    ai_msg = result['messages'][-1]
    st.write(file_taker.name)
    st.write(ai_msg.content)
    st.session_state.convo = result['messages']
