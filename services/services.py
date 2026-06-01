from api.client import APIClient

client = APIClient()


def fetch_all_posts():
    return client.get_all_posts()


def fetch_post(post_id):
    return client.get_post_by_id(post_id)


def add_post(title, body, user_id):
    return client.create_post(
        title,
        body,
        user_id
    )


def edit_post(post_id, title, body, user_id):
    return client.update_post(
        post_id,
        title,
        body,
        user_id
    )


def remove_post(post_id):
    return client.delete_post(post_id)