import requests 

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

response = requests.post(
                            endpoint,
                            params={"name": "John", "age": "30"},
                            json={"content": "trial"}
                        )

print(response.text)
# print(response.status_code)
# print(response.json())
