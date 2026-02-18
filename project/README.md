# JWT Authentication with FastAPI 🔐



## 📌 About

This repository demonstrates JSON Web Token (JWT) based authentication in a FastAPI application.  
It shows how to secure APIs using token-based authentication with `OAuth2PasswordBearer` and JWT, making the backend **stateless** and secure.

---

## 🔎 What Is JWT?

**JWT (JSON Web Token)** is a token-based authentication system used to:

- 🔑 Authenticate users  
- 🔐 Authorize access to protected routes  
- 📡 Make APIs stateless

### Why JWT?

Normally, HTTP does NOT remember who the user is (stateless).  
So after login, the server needs a way to *recognize the user* without storing session info.

JWT solves this by including user info inside a signed token that the client sends with every request.

---

## 📌 How JWT Works

### 1️⃣ Login Flow

Client → (login request) → API
API → create JWT token → send to Client
Client stores the token

So instead of the server *remembering* the user, the **client sends proof** (the JWT token) each time.

---

## 🔍 JWT Structure

A JWT has **3 parts**:


### 📌 Header
Contains:
- Algorithm used
- Token type  

### 📌 Payload
Contains data (like user ID, username).
⚠ **Important:** Payload is *not encrypted* — it’s only encoded.  
Do **NOT** put sensitive data here.

### 📌 Signature
Created using:
header + payload + SECRET_KEY


## 🚀 What I Implemented

This repository includes:

✅ JWT authentication flow  
✅ Login endpoint that returns a JWT  
✅ Protected routes using `OAuth2PasswordBearer`  
✅ Token verification logic  
✅ Stateless API authentication  

---

## 🛠 Technologies

- 🐍 Python  
- ⚡ FastAPI  
- 🔒 OAuth2PasswordBearer  
- 🧾 JWT (PyJWT or equivalent)

---

## 📍 How to Run

1. Clone the repository:
```bash
git clone <repo-url>
Create and activate virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies:

pip install -r requirements.txt
Run server:

uvicorn main:app --reload

