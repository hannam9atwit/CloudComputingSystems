# Michael's Cookbook – Lab 2 Express App

## Overview
This Express.js project expands my static cookbook website from Lab 1 into a dynamic NodeJS application. It serves static recipe pages and introduces five functional routes using query strings and path parameters.

## Structure
- `public/` – Contains static HTML pages: homepage, cookie recipe, banana bread recipe, and about
- `app.js` – Main Express application with dynamic routing
- `screenshots/` – Visual proof of working routes
- `README.md` – Project description and usage instructions

## Routes Demonstrated

### 1. `/recipe/:id`
- **Example:** `http://localhost:8000/recipe/cookie`
- **Description:** Displays either the cookie or banana bread recipe page based on the dish name.

### 2. `/comment/:dish`
- **Example:** `http://localhost:3000/comment/banana-bread`
- **Description:** Simulates leaving a comment for the selected dish.

### 3. `/greet`
- **Example:** `http://localhost:8000/greet?name=Michael`
- **Description:** Returns a personalized greeting using the `name` query string parameter.

### 4. `/feedback`
- **Example:** `http://localhost:8000/feedback?dish=cookie&rating=5`
- **Description:** Mimics a feedback submission with the dish name and rating passed as query strings.

### 5. `/about.html`
- **Example:** `http://localhost:8000/about.html`
- **Description:** Serves the static "About" page from the public folder.