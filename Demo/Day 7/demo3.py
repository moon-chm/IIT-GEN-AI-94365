from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool

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
    model='openai/gpt-oss-20b',
    model_provider='openai',
    base_url='http://10.186.172.93:1234/v1',
    api_key='none'
)
agent=create_agent(model=llm,tools=[calculator],system_prompt='You are an Expert in assistant the answer')
convo=[]
while True:
    user_promt=input("You: ")
    if user_promt == 'exit':
        break
    convo.append({
        'role':'user',
        'content':user_promt
    })
    result=agent.invoke({
        'messages':convo
    })
    llm_output=result['messages'][-1]
    print("AI: ",llm_output.content)
    convo=result['messages']