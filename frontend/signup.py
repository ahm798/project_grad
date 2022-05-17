import requests

endpoint = "http://127.0.0.1:8000/api/signup/"
data = {"username": "elliot", 'password':'hacker96', 'password2':'hacker96'}

response = requests.post(endpoint, json=data)


print(response.json())