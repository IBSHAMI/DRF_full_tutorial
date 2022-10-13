import requests

endpoint = "http://127.0.0.1:8000/api/products/"

response = requests.get(endpoint)

print(response.text)
# print(response.status_code)
# print(response.json())