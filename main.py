from api import get_posts
from utils import show_posts, posts_by_user, show_stats, view_post_details, save_posts, load_posts

posts = get_posts()

if not posts:
    print("Loading data from file...")
    posts = load_posts()
else:
    save_posts(posts)

while True:
    print("\n1. View posts")
    print("2. Filter by user")
    print("3. Show stats")
    print("4. View post details")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_posts(posts)
    elif choice == "2":
        user_id = int(input("Enter user ID: "))
        posts_by_user(posts, user_id)
    elif choice == "3":
        show_stats(posts)
    elif choice == "4":
        user_id = int(input("Enter a user ID: "))
        view_post_details(posts, user_id)
    elif choice == "5":
        break