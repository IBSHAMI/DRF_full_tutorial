import requests
from getpass import getpass

# get auth token
auth_endpoint = 'http://localhost:8000/api/auth/'
password = getpass()

auth_response = requests.post(auth_endpoint, json={
    "username": "staff",
    "password": password
}
)

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = "http://127.0.0.1:8000/api/products/"
    headers = {
        "Authorization": "Bearer " + token,
    }

    response = requests.get(endpoint, headers=headers)

    print(response.json())
