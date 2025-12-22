from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys
import time
st.header('Chat bot')
@tool
def scrap_data():
    """
    Docstring for scrap_data
    """
    driver=webdriver.Chrome()
    driver.get('https://www.sunbeaminfo.in/index')
    driver.implicitly_wait(7)
    search=driver.find_element(By.LINK_TEXT,"INTERNSHIP").click()
    time.sleep(5)
    table=driver.find_element(By.TAG_NAME,"table")
    rows=driver.find_element(By.TAG_NAME,"tr")
    time.sleep(2)
    data=[]
    for rows in table:
        cells=rows.find_element(By.TAG_NAME,'th')
        if not cells:
             cells=rows.find_element(By.TAG_NAME,'td')
        row_data=[cell.text for cell in cells]   
        data.append(row_data)  
    df = pd.DataFrame(data[1:], columns=data[0])  # use first row as header
print(df)    
   
    
    
llm=init_chat_model(
    model='openai/gpt-oss-20b',
    model_provider='openai',
    base_url='http://10.161.130.93:1234/v1',
    api_key='none' 
)
agent=create_agent(
    model=llm,
    tools=[],
    system_prompt="""you are an best question explainer ans summery but quality content"""
)
convo=[]
user_prompt=st.chat_input('Search something')
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
    st.write(ai_msg.content)
    convo=result['messages']