from api import get_posts
from utils import show_posts, posts_by_user, show_stats

posts = get_posts()

while True:
    print("\n1. View posts")
    print("2. Filter by user")
    print("3. Show stats")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_posts(posts)
    elif choice == "2":
        user_id = int(input("Enter user ID: "))
        posts_by_user(posts, user_id)
    elif choice == "3":
        show_stats(posts)
    elif choice == "4":
        break