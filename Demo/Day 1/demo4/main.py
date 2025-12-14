import streamlit as st
st.header("Welcome to Web Page")
st.title("This is Demo 4")
button=st.button("Click Me")

if button:
    st.write("Button Clicked!")
    st.balloons()

st.toggle("Show/Hide Text", key="toggle1")
if st.session_state.toggle1:
    st.write("You have toggled the text visibility!")
st.checkbox("Check Me", key="checkbox1")
if st.session_state.checkbox1:
    st.write("Checkbox is checked!")

#dropdown menu
options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Select an Option", options)    

