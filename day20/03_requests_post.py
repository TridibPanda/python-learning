import requests


url = "https://jsonplaceholder.typicode.com/posts"

payload = {"title": "Python Learning", "body": "Learning requests POST", "userId": 1}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response body:", response.json())
# Output:
# Status code: 201
# Response body: {'title': 'Python Learning', 'body': 'Learning requests POST', 'userId': '1', 'id': 101}
