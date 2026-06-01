import requests
from core.config import BASE_URL, HEADERS
from core.exceptions import *

def get_all_posts():

    try:

        response = requests.get(
            f"{BASE_URL}/posts",
            headers=HEADERS,
            timeout=5
        )

        if response.status_code == 404:
            raise NotFoundError(
                "Resource not found"
            )

        elif response.status_code == 401:
            raise UnauthorizedError(
                "Unauthorized access"
            )

        elif response.status_code >= 500:
            raise ServerError(
                "Server error"
            )

        return response.json()

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.ConnectionError:
        print("Network error")

    except APIError as e:
        print(e)

    except Exception:
        print("Unexpected error")

    return None

def get_post_by_id(post_id):

    try:
        response = requests.get(
            f"{BASE_URL}/posts/{post_id}",
            headers=HEADERS,
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def create_post(title, body, user_id):

    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    try:
        response = requests.post(
            f"{BASE_URL}/posts",
            headers=HEADERS,
            json=data,
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
    
def update_post(post_id, title, body, user_id):

    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    try:
        response = requests.put(
            f"{BASE_URL}/posts/{post_id}",
            headers=HEADERS,
            json=data,
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
    
def delete_post(post_id):

    try:
        response = requests.delete(
            f"{BASE_URL}/posts/{post_id}",
            headers=HEADERS,
            timeout=5
        )

        response.raise_for_status()

        return response.status_code

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None