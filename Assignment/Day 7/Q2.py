from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import json
import streamlit as st
import requests
load_dotenv('.env.local')
api_key=os.getenv('weather')

llm = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("API_KEY")
)
convo=[
    {
        'role':'system',
        'content':'Your are weather expert that explain anything about give weather data'
    }
]
st.header("Weather Info")
city=st.chat_input("Enter City name:")
if city:
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res=requests.get(url)
    weather=res.json()
    st.write("City name: ",city)
    st.write("Temperature: ", weather["main"]["temp"])
    st.write("Humidity: ", weather["main"]["humidity"])
    st.write("Wind Speed: ", weather["wind"]["speed"])
    llm_input = f"""
Question : {weather}
Instructions (VERY IMPORTANT):
Explain weather as you are an weather expert forcaster in english  
"""
    result = llm.invoke(llm_input)
    st.write(result.content)
