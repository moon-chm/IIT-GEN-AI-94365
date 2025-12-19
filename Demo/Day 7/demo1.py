from langchain.chat_models import init_chat_model
from langchain.agents import create_agent 
from dotenv import load_dotenv
import os
load_dotenv('.env.local')
llm=init_chat_model(
    model='openai/gpt-oss-120b',
    model_provider='openai',
    base_url='https://api.groq.com/openai/v1',
    api_key=os.getenv('API_KEY')
)
convo=[]
agent=create_agent(model=llm,tools=[],system_prompt='You are a helpful assistant. Answer in short.')
while True:
    user_prompt=input('You:  ')
    if user_prompt == "exit":
        break
    convo.append({
        'role':'user',
        'content':user_prompt
    })
    result=agent.invoke({
        'messages':convo
    })
    ai_msg=result['messages'][-1]
    print(ai_msg.content)
    convo=result['messages']