import requests

endpoint = "http://127.0.0.1:8000/api/products/delete/10/"

response = requests.delete(endpoint)

print(response.text)
# print(response.status_code)
# print(response.json())