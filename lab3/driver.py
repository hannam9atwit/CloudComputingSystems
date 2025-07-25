# driver.py
import requests

BASE = "http://127.0.0.1:8000"

def test_get_routes():
    print(requests.get(BASE + "/hello").json())
    print(requests.get(BASE + "/welcome", params={"name": "Michael"}).json())
    print(requests.get(BASE + "/recipe/cookie").json())
    print(requests.get(BASE + "/filter", params={"tag": "dessert", "difficulty": "medium"}).json())
    print(requests.get(BASE + "/rating/cookie").json())
    print(requests.get(BASE + "/convert", params={"grams": 100}).json())
    print(requests.get(BASE + "/review", params={"text": "Tasty and easy"}).json())
    print(requests.get(BASE + "/compare-time/pancakes/smoothie").json())
    print(requests.get(BASE + "/servings", params={"total": 12, "people": 4}).json())
    print(requests.get(BASE + "/ping").json())

def test_put_routes():
    profile_data = {"name": "Michael", "role": "Student"}
    comment_data = {"message": "Loved it!"}
    feedback_data = {"score": 9, "notes": "Excellent dish"}
    tips_reset_data = {"reset": True}
    settings_data = {"theme": "dark", "notifications": False}

    print(requests.put(BASE + "/profile/1", json=profile_data).json())
    print(requests.put(BASE + "/comment/cookie", json=comment_data).json())
    print(requests.put(BASE + "/feedback/Michael", json=feedback_data).json())
    print(requests.put(BASE + "/tips-reset/2", json=tips_reset_data).json())
    print(requests.put(BASE + "/settings", json=settings_data).json())

test_get_routes()
test_put_routes()
