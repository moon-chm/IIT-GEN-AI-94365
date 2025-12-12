import requests
api_key="e93897f7f9233d3eb5dbeff90e0a9fba"
city = input("Enter city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
print("status:", response.status_code)
weather = response.json()
print("Temperature:", weather['main']['temp'])