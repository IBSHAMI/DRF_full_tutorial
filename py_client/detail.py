import requests

endpoint = "http://127.0.0.1:8000/api/products/10/"

response = requests.get(
                            endpoint,
                            params={"name": "John", "age": "30"},
                            json={"content": "trial"}
                        )

print(response.text)
# print(response.status_code)
# print(response.json())