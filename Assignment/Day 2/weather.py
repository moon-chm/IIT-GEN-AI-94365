import requests
from dotenv import load_dotenv
import os
# Load .env.local
load_dotenv('.env.local')
api_key = os.getenv('API_KEY')
city = input("Enter city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
print("status:", response.status_code)
weather = response.json()
print("Temperature:", weather['main']['temp'])
