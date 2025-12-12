import requests

url="https://nilesh-g.github.io/learn-web/data/novels.json"
response = requests.get(url)
data = response.json()
print(data)
print("Request version: ",requests.__version__)