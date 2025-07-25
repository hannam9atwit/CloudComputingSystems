import requests

BASE_URL = "http://127.0.0.1:8000"

# Function to perform a GET request
def get_request(endpoint):
    response = requests.get(BASE_URL + endpoint)
    print(f"GET {endpoint}: {response.json()}")

# Function to perform a PUT request with a JSON payload
def put_request(endpoint, payload):
    response = requests.put(BASE_URL + endpoint, json=payload)
    print(f"PUT {endpoint}: {response.json()}")

# List of GET requests
get_endpoints = [
    "/helloworld",
    "/items/5?q=test",
    "/users/2?details=true",
    "/search?keyword=fastapi&limit=5",
    "/status",
    "/config/example",
    "/reports/2023",
    "/settings/theme",
    "/summary"
]

# Executing GET requests
for endpoint in get_endpoints:
    get_request(endpoint)

# List of PUT requests with example JSON payloads
put_endpoints = [
    ("/items/10", {"name": "Updated Item"}),
    ("/users/2", {"username": "new_user", "role": "admin"}),
    ("/modify/7", {"content": "Updated record content"}),
    ("/config/example", {"value": "dark mode"}),
    ("/reports/2023", {"report_data": {"sales": "increased", "growth": "stable"}}),
    ("/settings/theme", {"new_value": "light mode"})
]

# Executing PUT requests
for endpoint, payload in put_endpoints:
    put_request(endpoint, payload)

print("All API requests completed successfully.")
