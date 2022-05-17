import requests 

endpoint = "http://127.0.0.1:8000/api/home/"

response = requests.get(endpoint, params={'q':"helloWorld"} ,json={"query": "hello world"})


print(response.json())