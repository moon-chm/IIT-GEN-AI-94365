import pandas as pd
import streamlit as st
import pandasql as ps

st.header("CSV Data Viewer")

data = st.file_uploader("Upload your CSV file", type="csv")

if data:
    df = pd.read_csv(data)
    st.subheader("Uploaded CSV")
    st.dataframe(df)

    # SQL Query
    query = """
    SELECT SUM(price) as total_price,category
    FROM df group BY category
    """

    result = ps.sqldf(query, locals())

    st.subheader("SQL Query Result")
    st.dataframe(result)
