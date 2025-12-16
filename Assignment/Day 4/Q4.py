import streamlit as st
import os
import csv
import pandas as pd
import pandasql as ps

if 'page' not in st.session_state:
    st.session_state.page="Home"
if 'logged_in' not in st.session_state:
      st.session_state.logged_in=False
st.header("Welcome to Rohh's Web")

def auth_user(user_name,user_pass):
      if not os.path.exists('user.csv'):
            return False
      with open('user.csv','r',newline='')as file:
            reader=csv.reader(file)
            for row in reader:
                  if row[0]==user_name and row[1]==user_pass:
                        return True           
      return false           


def home_page():
    st.header("HOME PAGE")
    st.subheader("VENI VIDI VICI")

def login_page():
    st.header("Login")
    user_name=st.text_input("Enter Username: ")
    user_pass=st.text_input("Enter password: ",type="password")
    if st.button("Login"):
          if auth_user(user_name,user_pass):
                st.toast("Success")
                st.session_state.logged_in=True
                st.session_state.page="Explore CSV"
                st.rerun()
    else:
            st.toast("Failed!!")    

def register_page():
    st.header("Register Page")
    user_name=st.text_input("Enter Username: ")
    user_pass=st.text_input("Enter password: ",type="password")
    user_email=st.text_input("Enter Email: ")
    if st.button('Save'):
        with open("user.csv","a",newline="")as file:
            writer=csv.writer(file)
            writer.writerow([user_name,user_pass,user_email])
        st.toast("data stored!!")
        st.session_state.page="Login"   
        st.rerun()     
def explore_csv_page():
    st.header("Welcome to CSV")
    data=st.file_uploader("Browse the file",type='csv')
    if data:
          st.subheader("CSV File: ")
          df=pd.read_csv(data)
          st.dataframe(df)

def see_history_page():
    st.header("Welcome to history")

def logout_page():
    st.header("Logout Page") 
    st.session_state.logged_in=True
    st.session_state.page="Login"
    st.rerun() 

with st.sidebar:
    if not st.session_state.logged_in:
        if st.button("Home", use_container_width=True):
            st.session_state.page = "Home"
        if st.button("Login", use_container_width=True):
            st.session_state.page = "Login"
        if st.button("Register", use_container_width=True):
            st.session_state.page = "Register"
    else:
        if st.button("Explore CSV", use_container_width=True):
            st.session_state.page = "Explore CSV"
        if st.button("See History", use_container_width=True):
            st.session_state.page = "See History"
        if st.button("Logout", use_container_width=True):
            logout_page()

if st.session_state.page=="Home":
    home_page()
elif st.session_state.page=="Login":
    login_page()    
elif st.session_state.page=="Register":
    register_page()    
elif st.session_state.page=="Explore CSV":
                explore_csv_page()
elif st.session_state.page=="See History":
                see_history_page()
elif st.session_state.page=="Logout":
                 logout_page()      