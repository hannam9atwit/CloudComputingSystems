# Lab 8

## What the Program Does

- Initializes a FastAPI web server
- Defines a basic HTTP `GET` route: `/`
- Returns a JSON response: `{"message": "Hello, World from FastAPI + Docker!"}`
- Runs using Uvicorn
- Serves requests on port `8000`, accessible via `http://localhost:8000`

## How to Run It

1. Build the image:
   ```bash
   docker build -t lab8-image .