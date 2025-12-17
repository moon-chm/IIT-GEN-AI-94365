import streamlit as st
from chat_groq import chat_groq
from chat_local import chat_local

st.set_page_config(page_title="Chat Hub", layout="wide")

st.sidebar.title("Chat Selection")

page = st.sidebar.selectbox(
    "Choose Chat Model",
    ["Groq Cloud Chat", "Local LLM Chat"]
)

if page == "Groq Cloud Chat":
    chat_groq()
elif page == "Local LLM Chat":
    chat_local()
