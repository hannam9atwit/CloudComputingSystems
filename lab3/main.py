from fastapi import FastAPI, Request, Query, Path

app = FastAPI()

# Root route for connectivity check
@app.get("/")
def root():
    return {"message": "Hello from Michael's FastAPI Lab"}

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"}

# GET with query parameter for a personalized welcome
@app.get("/welcome")
def welcome(name: str = Query("guest")):
    return {"message": f"Welcome to the cookbook, {name}!"}

# GET with path parameter to return recipe details
@app.get("/recipe/{dish}")
def get_recipe(dish: str = Path(...)):
    return {"dish": dish, "instructions": f"Instructions for making {dish}"}

# PUT route to update user profile with body content
@app.put("/profile/{user_id}")
async def update_profile(user_id: int, request: Request):
    data = await request.json()
    return {"user_id": user_id, "profile": data}

# GET with multiple query parameters to filter recipes
@app.get("/filter")
def filter_tag(tag: str = Query(...), difficulty: str = Query("easy")):
    return {"tag": tag, "difficulty": difficulty}

# PUT to add a new comment to a dish
@app.put("/comment/{dish}")
async def add_comment(dish: str, request: Request):
    comment = await request.json()
    return {"dish": dish, "comment": comment}

# GET with path and logic to simulate star ratings
@app.get("/rating/{dish}")
def get_rating(dish: str):
    return {"dish": dish, "rating": 5 if dish == "cookie" else 4}

# GET to convert grams to ounces
@app.get("/convert")
def convert(grams: float = Query(...)):
    return {"grams": grams, "ounces": grams * 0.0353}

# PUT to submit feedback with user input
@app.put("/feedback/{username}")
async def submit_feedback(username: str, request: Request):
    data = await request.json()
    return {"user": username, "feedback": data}

# GET to echo a review string
@app.get("/review")
def review(text: str = Query(...)):
    return {"review": text}

# GET with two path parameters to compare preparation times
@app.get("/compare-time/{dish1}/{dish2}")
def compare_time(dish1: str, dish2: str):
    return {"comparison": f"{dish1} takes longer than {dish2} (example output)"}

# PUT to reset cooking tips for a user
@app.put("/tips-reset/{user_id}")
async def reset_tips(user_id: int, request: Request):
    payload = await request.json()
    return {"user_id": user_id, "reset": True, "data": payload}

# GET to divide servings
@app.get("/servings")
def divide_servings(total: int, people: int):
    if people == 0:
        return {"error": "Cannot divide by zero"}
    return {"servings_per_person": total / people}

# PUT to adjust recipe settings
@app.put("/settings")
async def update_settings(request: Request):
    data = await request.json()
    return {"updated_settings": data}

# GET ping test for debugging
@app.get("/ping")
def ping():
    return {"pong": "Server is responsive"}
