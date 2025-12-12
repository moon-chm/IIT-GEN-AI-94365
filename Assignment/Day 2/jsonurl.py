import requests
url="https://dummyjson.com/carts"
response = requests.get(url)
print("status:", response.status_code)
data = response.json()
print(data)