request = {
    "method": "GET",
    "url": "https://example.com/users",
    "headers": {"Authorization": "Bearer token"},
}

response = {
    "status_code": 200,
    "headers": {"Content-Type": "application/json"},
    "body": {"id": 1, "name": "John"},
}

print(f"Request method: {request['method']}")
print(f"Request URL: {request['url']}")

print(f"Response status: {response['status_code']}")
print(f"Response body: {response['body']}")

# Output:
# Request method: GET
# Request URL: https://example.com/users
# Response status: 200
# Response body: {'id': 1, 'name': 'John'}
