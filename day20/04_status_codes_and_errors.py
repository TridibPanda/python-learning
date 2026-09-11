import requests


def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = requests.get(url)

    print("Status code:", response.status_code)

    if response.status_code == 200:
        print(f"Success: {response.json()}")
    elif response.status_code == 404:
        print("Post not found")
    else:
        print("Request failed")


fetch_post(1)
# Output:
# Status code: 200
# Success: {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
fetch_post(9999)
# Output:
# Status code: 404
# Post not found
