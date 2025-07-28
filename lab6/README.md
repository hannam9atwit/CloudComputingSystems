# Lab 6

**Author:** Michael Hanna


---

## Introduction

This project builds a backend service using **FastAPI**, interfacing with the Guitar Shop MySQL database created in Lab 4.

---

## Project Description

The app defines 10+ routes:

- **GET** requests via query strings (e.g. filter by zip code or state)
- **PUT** requests with request bodies (e.g. update customer or product info)

The service runs locally using **Uvicorn**, and is designed for future deployment in containers or cloud-based architectures.

---

## Project Design

- `db_config.py`: Connects to the MySQL database securely  
- `models.py`: Pydantic models for request validation  
- `main.py`: FastAPI application logic — defines all routes  
- **GET routes** include:
  - `/products/` — fetch all products  
  - `/customers/` — list customers  
  - `/addresses/` — filter by state or city  
  - `/orders/` — retrieve item details  
  - ... and more  
- **PUT routes** include:
  - `/products/update` — update discount  
  - `/customers/update` — modify contact info  
  - `/addresses/update` — adjust zip codes  
  - `/orders/update` — quantity changes  
  - `/products/update_name` — rename by query string  