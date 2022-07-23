import requests

endpoint = "http://127.0.0.1:8000/api/products/product_update/4/"

data = {
    "title": "Hello World update",
    "price": 600
}

response = requests.put(endpoint, json=data)

print(response.json())