from dotenv import load_dotenv
import os
import responses
import getinfo

load_dotenv('.env.local')

api_key = os.getenv('API_KEY')
city = input("Enter city name: ")

response = responses.getweather(api_key, city)

temp = getinfo.gettemp(response)
humidity = getinfo.gethumidity(response)
wind = getinfo.getwind(response)
timezone = getinfo.gettimezone(response)

print(f"Temperature: {temp}°C")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind} m/s")
print(f"Timezone: {timezone}")
