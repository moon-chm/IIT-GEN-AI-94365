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
    """
     This get_weather() function gets the current weather of given city.
    If weather cannot be found, it returns 'Error'.
    This function doesn't return historic or general weather of the city.

    :param city: str input - city name
    :returns current weather in json format or 'Error'  
    """
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
    """
    This calculator function solves any arithmetic expression containing all constant values.
    It supports basic arithmetic operators +, -, *, /, and parenthesis. 
    
    :param expression: str input arithmetic expression
    :returns expression result as str
    """
    try:
        result=eval(expression)
        return str(result)
    except:
        print('Error')

llm=init_chat_model(
    model='google/gemma-3-4b',
    model_provider='openai',
    base_url='http://127.0.0.1:1234/v1',
    api_key='none'
)
agent=create_agent(model=llm,tools=[weather,calculator],
                   system_prompt="Your are expert short answer assistent")
convo=[]

user_prompt=st.chat_input("Search Something: ")
if user_prompt:
    convo.append(
        {
            'role':'user',
            'content':user_prompt
        }
    )
    result=agent.invoke(
        {
            'messages':convo
        }
    )
    ai_msg=result['messages'][-1]
    st.write(user_prompt)
    st.write(ai_msg.content)
    convo=result['messages']
