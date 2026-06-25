import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    try:
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error", e)
        return []
    
