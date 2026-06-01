from services.services import *


while True:

    print("\nREST API CLIENT")

    print("1. Fetch all posts")
    print("2. Fetch post by ID")
    print("3. Create post")
    print("4. Update post")
    print("5. Delete post")
    print("6. Exit")

    choice = input("Enter choice: ")


    if choice == "1":

        posts = fetch_all_posts()

        if posts:
            for post in posts[:5]:
                print(post)


    elif choice == "2":

        post_id = input("Enter post ID: ")

        if not post_id.isdigit():
            print("Invalid ID. Enter numbers only")

        else:
            post = fetch_post(post_id)

            if post:
                print(post)


    elif choice == "3":

        title = input("Title: ")
        body = input("Body: ")
        user_id = input("User ID: ")

        post = add_post(
            title,
            body,
            user_id
        )

        print(post)


    elif choice == "4":

        post_id = input("Post ID: ")
        title = input("Title: ")
        body = input("Body: ")
        user_id = input("User ID: ")

        post = edit_post(
            post_id,
            title,
            body,
            user_id
        )

        print(post)


    elif choice == "5":

        post_id = input("Post ID: ")

        if not post_id.isdigit():
            print("Invalid ID")

        else:

            result = remove_post(post_id)

            print(
                "Deleted Successfully"
                if result
                else "Delete failed"
            )


    elif choice == "6":

        print("Exiting...")
        break


    else:
        print("Invalid Choice")