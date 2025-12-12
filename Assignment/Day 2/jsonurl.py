import requests
url="https://dummyjson.com/carts"
response = requests.get(url)
print("status:", response.status_code)
data = response.json()
print(data)
#get specific cart data with id
import json

cart_id = input("Enter cart id (1-13): ")
specific_url = f"{url}/{cart_id}"

try:
    specific_response = requests.get(specific_url)
    print("status:", specific_response.status_code)
    
    if specific_response.status_code == 404:
        print("Error: Cart ID not found. Valid IDs are 1-13")
    else:
        specific_data = specific_response.json()
        print(specific_data)
        
        #save fetch data to file 
        with open("cart_data.json","w") as file:
            json.dump(specific_data, file, indent=4)
        print("Data saved to cart_data.json")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")