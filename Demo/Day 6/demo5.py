from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv('.env.local')
llm=init_chat_model(
    model='openai/gpt-oss-120b',
    model_provider='openai',
    base_url='https://api.groq.com/openai/v1',
    api_key=os.getenv('API_KEY')
)
convo=[{'role':'system','content':'Your are an health expert'}]
while True:
    user_promt=input("Search something")
    if user_promt=='exit':
        break
    convo.append({'role': 'user', 'content': user_promt})
    llm_output=llm.invoke(convo)
    print('Ai: ',llm_output.content)
    llm_msg={'role':'assistant','content':llm_output.content}
    convo.append(llm_msg)