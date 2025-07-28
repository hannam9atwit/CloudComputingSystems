# Lab 7

This lab sets up a multi-service phone accessory storefront using Docker containers and the Backend-for-Frontend (BFF) pattern. It explores modular microservices that divide responsibilities across authentication, product browsing, and order management.

---

## What the Program Does

- Implements a modular API ecosystem with clear service boundaries
- Uses Docker to isolate each component:
  - Authentication
  - Product Catalog
  - Order Processing
- Applies the BFF pattern for tailored client responses
- Coordinates multiple containers with `docker-compose`

Each module is designed to be independently deployable, scalable, and testable in isolation — ideal for real-world service-oriented applications.