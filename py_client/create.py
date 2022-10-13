import requests

endpoint = "http://127.0.0.1:8000/api/products/create/"

response = requests.post(
                            endpoint,
                            params={"name": "John", "age": "30"},
                            json={"title": "new tutorial", "content": "trial"}
                        )

print(response.text)
# print(response.status_code)
# print(response.json())