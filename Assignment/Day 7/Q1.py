from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import pandas as pd
import streamlit as st
import pandasql as ps
load_dotenv('.env.local')

llm = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("API_KEY")
)

convo = [
    {
        'role': 'system',
        'content': 'Your are an SQLite expert of 10 years master in database sql'
    }
]

csv = st.file_uploader('Upload csv file', type='csv')

if csv:
    df = pd.read_csv(csv)
    st.dataframe(df)
    data=df

    user_prompt = st.chat_input('Ask anything about this csv')

    if user_prompt:
        llm_input = f"""
Table Name : data
Table Schema : {df.dtypes}
Question : {user_prompt}
Instructions (VERY IMPORTANT):
1. First line: output ONLY a valid SQLite SQL query in plain text.
2. Do NOT use markdown, backticks, or code blocks.
3. Do NOT add any text before or after the SQL query on the first line.
4. After the SQL query, on a new line write:
   EXACT_VALUE:
   followed by the exact result based on the table data if it can be computed, otherwise write UNKNOWN.
5. After that, on a new line write:
   EXPLANATION:
   followed by a simple English explanation of what the query does.
6. If a valid SQL query cannot be generated, output exactly:
   Error
"""
        result = llm.invoke(llm_input)
        st.write(result.content)
        sql_query = result.content.splitlines()[0].strip()
        sqloutput = ps.sqldf(sql_query, locals())
        st.dataframe(sqloutput)