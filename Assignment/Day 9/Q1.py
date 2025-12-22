import streamlit as st
import pandas as pd
import pandasql as ps
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Multi-Agent Chat App", layout="wide")
st.header("🤖 Multi-Agent Chat App")
st.markdown("This app has two agents:\n- CSV Q&A Agent\n- Sunbeam Web Scraper Agent\nAll chat history is preserved.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

csv_file = st.file_uploader("Upload a CSV file", type="csv")
user_input = st.text_input("Ask your question:")

@st.cache_data
def load_csv(file):
    return pd.read_csv(file)

@tool
def csv_explain(query: str):
    """
    Convert user question into SQL, run it using pandasql, and return the result.
    """
    if not csv_file:
        return {"error": "No CSV file uploaded"}
    
    df = load_csv(csv_file)
    data = df

    llm_input = f"""
Table Name: data
Schema: {df.dtypes}
Question: {query}
Instructions: Generate a valid SQLite SQL query to answer the question.
Output ONLY the SQL query. If impossible, output Error.
"""
    sql_query = llm.invoke(llm_input).content.splitlines()[0].strip()

    if sql_query == "Error":
        return {"error": "Could not generate a valid SQL query"}

    try:
        sqloutput = ps.sqldf(sql_query, {"data": data})
        if not sqloutput.empty:
            first_col = sqloutput.columns[0]
            sqloutput = sqloutput.sort_values(by=first_col, ascending=True).reset_index(drop=True)
    except Exception as e:
        return {"error": str(e)}

    return {"sql": sql_query, "data": sqloutput}

@tool
def sunbeam_scraper(query: str):
    """
    Scrape Sunbeam internship and batch info.
    """
    url = "https://www.sunbeaminfo.in/index" 
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": f"Failed to access website (status {response.status_code})"}
        soup = BeautifulSoup(response.text, "html.parser")

        internships = [item.text.strip() for item in soup.select(".internship-card h3")]
        batches = [item.text.strip() for item in soup.select(".batch-info")]

        info_text = f"Internships:\n{internships}\nBatches:\n{batches}"
        return {"data": info_text}
    except Exception as e:
        return {"error": str(e)}

llm = init_chat_model(
    model="google/gemma-3-4b",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="none"
)
csv_agent = create_agent(
    model=llm,
    tools=[csv_explain],
    system_prompt="You are a CSV expert. Only use the csv_explain tool. No natural language answers."
)

web_agent = create_agent(
    model=llm,
    tools=[sunbeam_scraper],
    system_prompt="You are a web scraping assistant. Only use sunbeam_scraper tool."
)

if user_input:
    if "csv" in user_input.lower() or csv_file:
        output = csv_agent.invoke({"messages": [("user", user_input)]})
    else:
        output = web_agent.invoke({"messages": [("user", user_input)]})

    content = output["messages"][-1].content
    st.session_state.chat_history.append(("User", user_input))
    st.session_state.chat_history.append(("Agent", content))

for sender, message in st.session_state.chat_history:
    if sender == "User":
        st.markdown(f"**You:** {message}")
    else:
        if isinstance(message, dict):
            if "error" in message:
                st.error(message["error"])
            elif "sql" in message:
                st.subheader("🧠 Generated SQL")
                st.code(message["sql"], language="sql")
                st.subheader("📄 Query Result")
                st.dataframe(message["data"], use_container_width=True)
            else:
                st.subheader("📄 Data")
                st.text(message.get("data", "No data"))
        else:
            st.markdown(f"**Agent:** {message}")
