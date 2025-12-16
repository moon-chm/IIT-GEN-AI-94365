import streamlit as st

with st.form(key="log_form"):
    st.header("Login")
    user_name=st.text_input("Enter User Name: ")
    user_pass=st.text_input("Enter User password: ",type="password")
    age=st.slider("Select age",1,100,25,1)
    addr=st.text_area("Enter Address")
    sbt_btn=st.form_submit_button("Submit")

if sbt_btn:
    err_msg=""
    is_error=False
    if not user_name:
        is_error=True
        err_msg+="Not User Name can be empty"
    if not user_pass:
        is_error=True
        err_msg+="Not User Password can be empty"    
    if not age:
        is_error=True
        err_msg+="Not User age can be empty"            
    if not addr:
        is_error=True
        err_msg+="Not User Address can be empty"

    if is_error:
        st.error(err_msg)   
    else:
        msg=f"Successfully logged in {user_name} welcome to website"
        st.success(msg)         
