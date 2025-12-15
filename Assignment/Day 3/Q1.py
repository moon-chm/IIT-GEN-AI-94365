import streamlit as st
import pandas as pd
import pandasql as ps

st.title("Welcome to CSV READ!!")
data=st.file_uploader("Upload the CSV file",type='csv')
if data:
    df=pd.read_csv(data)
    st.subheader('Uploaded CSV')
    st.dataframe(df)

query="""
select sum(quantity),category from df group by category 
"""    
result=ps.sqldf(query,locals())
st.dataframe(result)