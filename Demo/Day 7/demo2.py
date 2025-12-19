from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

llm=init_chat_model(
    model='openai/gpt-oss-20b',
    model_provider='openai',
    base_url='http://10.186.172.93:1234/v1',
    api_key='none'
)
convo=[]
agent=create_agent(model=llm,tools=[],system_prompt='You are best ai assistant to ans help in short best answer')
while True:
    user_prompt=input('You:')
    if user_prompt == 'exit':
        break
    convo.append(
        {
            'role':'user',
            'content':user_prompt
        }
    )
    result=agent.invoke({
        'messages':convo
    })
    ai_msg=result['messages'][-1]
    print("AI: ",ai_msg.content)
    convo=result['messages']
