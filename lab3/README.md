# Lab 3 – FastAPI Application  
**Author:** Michael Hanna

## Introduction  
This project is part of Lab 3 for a web development course. It builds on previous labs by implementing a backend application using FastAPI and Uvicorn. The app simulates cookbook-style interactions, allowing users to view and manipulate recipe, feedback, and profile data through RESTful routes.

## Description  
- Developed using Python with FastAPI and Uvicorn  
- Includes 15+ working routes using GET and PUT methods  
- Routes support query strings, path parameters, and JSON body inputs  
- Organized and annotated code for clarity and maintainability  
- A Python test driver script (`driver.py`) sends sample requests to each endpoint  

## Design  
- `main.py`: Core FastAPI server with routes  
- `driver.py`: Python script to test all API functionality  
- Routes cover user profiles, recipe data, comments, feedback, filtering, conversion, and utility endpoints  
- Uses `Request` for body parsing and `Query` / `Path` for input validation  


## Route Overview  

### GET Routes  
| Endpoint                        | Example URL                           | Description                          |
|---------------------------------|---------------------------------------|--------------------------------------|
| `/hello`                        | `/hello`                              | Basic server greeting                |
| `/welcome`                      | `/welcome?name=Michael`               | Personalized greeting                |
| `/recipe/{dish}`                | `/recipe/cookie`                      | Retrieve recipe instructions         |
| `/filter`                       | `/filter?tag=dessert&difficulty=easy` | Filter recipes by tag and difficulty |
| `/rating/{dish}`                | `/rating/cookie`                      | Simulate dish rating                 |
| `/convert`                      | `/convert?grams=100`                  | Convert grams to ounces              |
| `/review`                       | `/review?text=Tasty`                  | Echo a review text                   |
| `/compare-time/{dish1}/{dish2}` | `/compare-time/soup/salad`            | Compare prep time                    |
| `/servings`                     | `/servings?total=8&people=2`          | Divide servings                      |
| `/ping`                         | `/ping`                               | Debug route, returns server status   |

### PUT Routes  
| Endpoint                | Body Fields                    | Description             |
|-------------------------|--------------------------------|-------------------------|
| `/profile/{user_id}`    | JSON with `name`, `role`, etc. | Update user profile     |
| `/comment/{dish}`       | JSON with `message`            | Add comment to dish     |
| `/feedback/{username}`  | JSON with feedback content     | Submit feedback         |
| `/tips-reset/{user_id}` | JSON with reset state          | Reset cooking tips      |
| `/settings`             | JSON with settings data        | Update general settings |



