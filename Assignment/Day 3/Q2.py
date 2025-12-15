import streamlit as st
from dotenv import load_dotenv
import os
import requests

load_dotenv(".env.local")
api_key = os.getenv("API_KEY")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"


def login_page():
    st.title("Login Page")

    username = st.text_input("Enter User Name")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        if username == "Rohit" and password == "Rohit123":
            st.session_state.logged_in = True
            st.session_state.page = "weather"
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid Credentials")


def weather_page():
    st.title("Weather Information")

    city = st.text_input("Enter City Name")

    if st.button("Get Weather"):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if data.get("cod") == 200:
                st.subheader(f"Weather in {city.title()}")
                st.write("Temperature:", data["main"]["temp"], "°C")
                st.write("Humidity:", data["main"]["humidity"], "%")
                st.write("Condition:", data["weather"][0]["description"])
            else:
                st.error("City not found")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.rerun()


if st.session_state.page == "login":
    login_page()

elif st.session_state.page == "weather":
    if st.session_state.logged_in:
        weather_page()
    else:
        st.session_state.page = "login"
        st.rerun()
