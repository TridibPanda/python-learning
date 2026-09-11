import requests


def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        print(f"Status: {response.status_code}")
        print(f"Data: {data}")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")


fetch_post(5)
# Output:
# Status: 200
# Data: {'userId': 1, 'id': 5, 'title': 'nesciunt quas odio', 'body': 'repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque'}
fetch_post(2000)
# Output:
# HTTP error: 404 Client Error: Not Found for url: https://jsonplaceholder.typicode.com/posts/2000
