import streamlit as st
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
if 'message' not in st.session_state:
    st.session_state.message=[]

st.title("Langchain Bot:")
load_dotenv('.env.local')
llm=init_chat_model(
    model='llama-3.3-70b-versatile',
    model_provider='openai',
    base_url='https://api.groq.com/openai/v1',
    api_key=os.getenv('API_KEY'))
user_prompt=st.chat_input("Search something..")
if user_prompt:
    result=llm.stream(user_prompt)
    st.session_state.message.append(user_prompt)
    st.session_state.message.append(result)  
    msg_list=st.session_state.message  
    for idx,result in enumerate(msg_list):
     role="user" if idx % 2==0 else "ai"
     with st.chat_message(role): 
        st.write(result)