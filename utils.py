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