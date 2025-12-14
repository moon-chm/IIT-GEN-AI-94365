import streamlit as st
import time
st.title("Hello, All!!")
st.header("DSSA")
st.write("Hello Pune, Air and people are very cold")

if st.button("Click Me!!", type="primary"):
    st.toast("You clicked me...")
    #st.balloons()
    #st.snow()
    with st.spinner("wait for it"):
        time.sleep(2)
    st.write("Got it....")
    st.success('Done!')
