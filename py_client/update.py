import requests

endpoint = "http://127.0.0.1:8000/api/products/update/10/"

data = {
    'title': 'New title',
    'content': 'New content',
    'price': 19,
}

response = requests.put(endpoint, json=data)

print(response.text)
# print(response.status_code)
# print(response.json())