import requests


url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

"""
requests.get()
      ↓
Response object
      ├── status_code
      ├── headers
      ├── text
      ├── content
      └── json()
"""


print("Status code:", response.status_code)
print("Response headers:", response.headers)
print("Response body:", response.json())
# Output:
# Status code: 200
# Response headers: {'Date': 'Fri, 11 Sep 2026 07:50:11 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'access-control-allow-credentials': 'true', 'Cache-Control': 'max-age=43200', 'etag': 'W/"124-yiKdLzqO5gfBrJFrcdJ8Yq0LGnU"', 'expires': '-1', 'nel': '{"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}', 'pragma': 'no-cache', 'report-to': '{"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=QwcX6nLtJ2b6%2BABQIX1mfYF8MxKJ69sRv8nTGsMQs8o%3D\\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\\u0026ts=1785189191"}],"max_age":3600}', 'reporting-endpoints': 'heroku-nel="https://nel.heroku.com/reports?s=QwcX6nLtJ2b6%2BABQIX1mfYF8MxKJ69sRv8nTGsMQs8o%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1785189191"', 'Server': 'cloudflare', 'vary': 'Origin, Accept-Encoding', 'via': '2.0 heroku-router', 'x-content-type-options': 'nosniff', 'x-powered-by': 'Express', 'x-ratelimit-limit': '1000', 'x-ratelimit-remaining': '999', 'x-ratelimit-reset': '1785189203', 'Age': '6283', 'cf-cache-status': 'HIT', 'Content-Encoding': 'gzip', 'CF-RAY': 'a3951482f9f5e1d9-MRS', 'alt-svc': 'h3=":443"; ma=86400'}
# Response body: {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
