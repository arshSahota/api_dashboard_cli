import json

def show_posts(posts):
    for i, post in enumerate(posts[:5], start=1):
        print(f"{i}. {post['title']}")

def posts_by_user(posts, user_id):
    for post in posts:
        if post["userId"] == user_id:
            print(post["title"])

def show_stats(posts):
    total = len(posts)
    users = set()

    for post in posts:
        users.add(post["userId"])

    print(f"Total posts: {total}")
    print(f"Unique users: {len(users)}")

def view_post_details(posts, post_id):
    for post in posts:
        if post["id"] == post_id:
            print(f"\nTitle: {post['title']}")
            print(f"Body: {post['body']}")
            print(f"User ID: {post['userId']}")
            return
    print("Post not found.")

def save_posts(posts):
    with open("posts.json", "w") as f:
        json.dump(posts, f, indent=4)

def load_posts():
    try:
        with open("posts.json", "r") as f:
            return json.load(f)
    except:
        return []