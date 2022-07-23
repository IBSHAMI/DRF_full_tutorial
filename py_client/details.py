import requests

endpoint = "http://127.0.0.1:8000/api/products/product_detail/4/"

response = requests.get(endpoint)

print(response.json())