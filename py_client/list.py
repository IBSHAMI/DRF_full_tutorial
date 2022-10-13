import requests
import getpass


endpoint = "http://127.0.0.1:8000/api/auth/"
password = getpass.getpass()

auth_response = requests.post(endpoint, json={
    "username": "staff",
    "password": password
})

# return back the data from the response
# will include the token for the user
print(auth_response.json())


# after we get the token we can use it to make requests
if auth_response.status_code == 200:
    token = auth_response.json().get('token')
    if token is not None:
        # make a request with the token
        auth_headers = {
            'Authorization': 'Token ' + token
        }
        endpoint = "http://127.0.0.1:8000/api/products/"
        # get request
        response = requests.get(endpoint, headers=auth_headers)

        print(response.text)

