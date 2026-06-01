from client import (
    get_all_posts,
    get_post_by_id,
    create_post,
    update_post,
    delete_post
)


def fetch_all_posts():
    return get_all_posts()


def fetch_post(post_id):
    return get_post_by_id(post_id)


def add_post(title, body, user_id):
    return create_post(title, body, user_id)


def edit_post(post_id, title, body, user_id):
    return update_post(
        post_id,
        title,
        body,
        user_id
    )


def remove_post(post_id):
    return delete_post(post_id)