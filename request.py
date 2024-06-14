import requests

url = "http://localhost:8000/arithmatic/"
payload = {
    "op": 'add',
    "num1": 24,
    "num2": 12
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
