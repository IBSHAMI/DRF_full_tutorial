import requests

product_id = input("what is the id ?")

endpoint = f"http://127.0.0.1:8000/api/products/product_delete/{product_id}/"

response = requests.delete(endpoint)

# it will return 204 status code if successful
print(response.status_code) 
# print(response.json())