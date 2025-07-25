# Lab 5 – Guitar Shop SQL Queries in Python  
**Author:** Michael Hanna

## Introduction  
This lab builds on Lab 4 by reimplementing SQL queries from the Guitar Shop database using Python functions and validating them with unit tests. It demonstrates how backend logic can interface with a relational database and maintain testable, modular code.

## Project Description  
- **Database**: `guitar_shop`, created in Lab 4 and accessed via Python 
- **Libraries Used**: `mysql.connector`, `unittest`
- **Structure**:
  - SQL logic broken into Python functions
  - Each query wrapped in a testable function
  - Unit tests verify correctness and output format

## Project Design  
- `db_config.py` — manages MySQL connection  
- `queries.py` — contains Python functions for 7 SQL queries  
- `test_queries.py` — uses Python `unittest` to validate each query function  
