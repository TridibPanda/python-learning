```text
Client
  │
  │ HTTP Request
  │ GET /users
  │ headers
  ↓
Server
  │
  │ HTTP Response
  │ status code
  │ headers
  │ body
  ↓
Client
```
```text
GET
→ retrieve

POST
→ create

PUT
→ replace/update

PATCH
→ partial update

DELETE
→ delete
```

### Q1. In a backend application, why should we check the HTTP status code before assuming that the response body contains the successful data?
We check the status code to determine whether the HTTP request succeeded before treating the response body as successful data.

There are multiple successful HTTP statuses:
```
200 OK
201 Created
202 Accepted
204 No Content
```
And failures include:
```
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```
### Q2. Why does HTTPError get handled before the more general RequestException?
HTTPError isn't specifically for "request info errors"; it's for an HTTP response with a 4xx or 5xx status. RequestException is the broader base class covering requests-related exceptions, including HTTPError, Timeout, connection errors, etc.