# Backend Phase 1 🚀  
* FastAPI Training Project*

This repository contains backend development work done during a structured FastAPI training.  
 The goal is to build a production-ready FastAPI app with database integration and proper API design.

---

## 📋 Table of Contents

 
  - [Day 1 – FastAPI Fundamentals](#day-1-fastapi-fundamentals)  
  - [Day 2 – Pydantic & Validation](#day-2-pydantic-&-validation)  
  - [Day 3 – Database & CRUD](#day-3-database-&-crud)  
  - [Day 4 – Full Fledged Project](#day-4-full-fledged-project)  

---


### 🗓 Day 1 – FastAPI Fundamentals

**Concepts Covered:**

- **What is FastAPI?**

Fast api is a  modern and fast web framework for building APIs with Python. 
API = Application Programming Interface → It allows two applications to communicate with each other. 
It is based on Python type hints, which makes your code cleaner and reduces bugs. 
----Python is a dynamically typed language → normally, you don’t have to declare the type of a variable.Type hints let you optionally specify the type of variables, function parameters, and return values.They help humans and tools (like editors, linters, and FastAPI) understand your code better, but Python itself does not enforce types at runtime 
Example
age: int = 25

# String type
name: str = "Mubeen"
def add(a: int, b: int) -> int:
    return a + b

result = add(5, 10)
print(result)

-> int means this function returns an integer.

-**ASGI vs WSGI (high-level)**

# WSGI = Web Server Gateway Interface
It’s a standard “bridge” between Python web apps and web servers.Basically: WSGI tells Python how to talk to the web server and vice versa.
WSGI is synchronous:
-Handles one request at a time per thread/process.
-Good for normal web pages where users just request HTML or JSON.
-Not ideal for real-time apps like chat, WebSockets, or live updates.
How it works:

Browser -> Web Server -> WSGI Interface -> Python App -> WSGI -> Web Server -> Browser
 The WSGI interface defines how the server passes requests to Python and how Python sends back responses.

- Installing FastAPI + Uvicorn
- Basic app structure
- HTTP methods (GET, POST, PUT, DELETE)
- Path parameters
- Query parameters
- Request body
- Automatic docs (Swagger)
# What is ASGI?
ASGI = Asynchronous Server Gateway Interface
It’s the modern version of WSGI, designed for both synchronous and asynchronous apps.Supports real-time features like:
-WebSockets (chat apps, live updates)
-Background tasks
Key points about ASGI
-ASGI is asynchronous:
-Can handle many requests at the same time.
-Works with modern web frameworks like FastAPI, Starlette, Django Channels.
How it works:

Browser -> ASGI Server -> ASGI Interface -> Python App -> ASGI -> Server -> Browser

**Mini Project – Simple Task API**

Build endpoints:

- `GET /` → Welcome message  
- `GET /tasks` → Return list of tasks  
- `POST /tasks` → Add a task  
- `GET /tasks/{task_id}` → Get a single task  
- `DELETE /tasks/{task_id}` → Delete a task



---

### 🗓 Day 2 – Pydantic + Validation + Structure

**Concepts Covered:**

- # Pydantic models
Purpose: Define data structure + validation for requests and responses.
Pydantic ensures the data matches the expected type and automatically raises errors for invalid input.

- # Request validation

FastAPI automatically validates incoming request data using Pydantic models. 
Wrong type → automatic error
Missing required field → automatic error

- # Response models
what you api returns
sometime we donot want to return all data like 

- # Status codes
FastAPI allows you to set correct HTTP status codes. 
200 → OK
201 → Created
404 → Not Found
400 → Bad Request

from fastapi import status

- # HTTPException: used to raise errors manually.
- # Modular structure
    • Keeps code organized
    • Makes it scalable and maintainable
    • Each file has a single responsibility

- # APIRouter
Used to separate routes into modules. 
from fastapi import APIRouter

- # Environment variables:
Purpose: create a separate file to store secrets/configuration safely (DB URLs, API keys, secret keys). 


**Mini Project – Refactor Task API**

Include:

- Pydantic models: `TaskCreate`, `TaskResponse`
- Validation: title must be 3+ characters
- Proper status codes
- Routes in APIRouter

---

### 🗓 Day 3 – Database + CRUD + Async

**Concepts Covered:**

- What is ORM?
ORM (Object–Relational Mapping) is a technique that allows you to interact with a relational database using programming language objects (like Python classes) instead of writing raw SQL queries.


- DB connection with FastAPI

Two main things:
-sqlalchemy → ORM
ORM (like SQLAlchemy) is a tool that converts your Python objects into SQL queries.
-psycopg2-binary → PostgreSQL driver (connector)
A database driver is like a translator/connector between Python and the actual database (PostgreSQL, MySQL, etc.).
    • Examples for PostgreSQL: psycopg2, asyncpg.
    • Examples for MySQL: mysqlclient, pymysql.

 Install Required Packages 
pip install fastapi uvicorn sqlalchemy psycopg2-binary


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "postgresql://username:password@localhost/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Explanation
    • create_engine() → Connects SQLAlchemy to PostgreSQL
    • SessionLocal → Creates database sessions
    • Base → Parent class for all ORM models
Think of Base as foundation of all tables.


**Mini Project – Task API with Database**

Tasks to implement:

- Connect PostgreSQL
- Create `Task` table
- CRUD endpoints using DB and dependency injection



### 🗓 Day 4 – Full Fledged Project

**Final Project – Mini Project Management System**

Users can:

- Register and login
- Create projects
- Create tasks within projects

Tasks have statuses: `pending`, `in_progress`, `completed`

**Routes to Implement:**

**User Module**  
- `POST /users/register`  
- `POST /users/login`

**Project Module**  
- `POST /projects`  
- `GET /projects`  
- `GET /projects/{id}`  
- `DELETE /projects/{id}`

**Task Module**  
- `POST /projects/{id}/tasks`  
- `GET /projects/{id}/tasks`  
- `PUT /tasks/{task_id}`  
- `DELETE /tasks/{task_id}`

**Database Design:**

| Table | Columns |
|-------|---------|
| User | id, username, email, password |
| Project | id, name, description, owner_id |
| Task | id, title, description, status, project_id |

---

## 📁 Project Structure (Final)

