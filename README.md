Backend Assignment – FastAPI + MongoDB + Ngrok 

This project implements a **cloud-based backend system** using **FastAPI**, **MongoDB Atlas**, and **Ngrok** for public exposure.  
It was developed as part of the backend assignment to demonstrate:

- REST API development  
- Cloud database integration  
- Secure password hashing  
- Modular backend structure  
- API testing using Swagger  

---

1. Project Features**

### ✔ FastAPI backend  
### ✔ MongoDB Atlas connection  
### ✔ Organization creation endpoint  
### ✔ Password hashing (bcrypt)  
### ✔ Modular folder structure  
### ✔ Fully tested using Swagger UI  
### ✔ Exposed publicly using Ngrok  

---

2. Project Folder Structure**

```
backend/
│
├── app/
│   ├── main.py          # FastAPI application
│   ├── routes.py        # API routes/endpoints
│   ├── models.py        # Pydantic models
│   ├── database.py      # MongoDB connection
│   ├── config.py        # Secrets (placeholders)
│
├── requirements.txt      # Project dependencies
├── README.md             # Documentation
├── .gitignore            # Ignored files
```

---
3. Technologies Used**

| Technology | Purpose |
|-----------|----------|
| **FastAPI** | Backend framework |
| **MongoDB Atlas** | Cloud database |
| **Motor (Async MongoDB Client)** | Async DB operations |
| **Pyngrok** | Public URL for testing |
| **Uvicorn** | FastAPI server |
| **Passlib (bcrypt)** | Password hashing |
| **Pydantic** | Data validation |

---

4. API Endpoints**

POST /org/create**
Creates a new organization.

### Request Body:
```json
{
  "organization_name": "my_company",
  "email": "owner@company.com",
  "password": "mypassword123"
}
```

### Responses:
| Status | Meaning |
|--------|----------|
| **200** | Organization created |
| **400** | Email already exists |
| **500** | Server error (DB issue, validation issue, etc.) |

---

5. How to Set Up the Project**

Step 1 — Install libraries**
```
pip install -r requirements.txt
```

---

Step 2 — Configure MongoDB Atlas**

1. Go to: https://cloud.mongodb.com  
2. Create a cluster  
3. Create a database user  
4. Allow IP access: `0.0.0.0/0`  
5. Copy your connection string:

```
mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/
```

6. Open `app/config.py` and replace:

```python
MONGO_URI = "YOUR_MONGO_URI_HERE"
JWT_SECRET = "YOUR_SECRET_KEY"
```

---

Step 3 — Run FastAPI**

```
uvicorn app.main:app --reload
```

Server runs on:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

Step 4 — Make API Public (Ngrok)**

1. Install ngrok  
2. Set your token:

```
ngrok config add-authtoken YOUR_TOKEN
```

3. Run:

```
ngrok http 8000
```

You will get:

```
https://xxxx.ngrok-free.dev
```

Use:

```
https://xxxx.ngrok-free.dev/docs
```

to test your APIs online.

---
6. Explanation of Each File**

### 🔹 **main.py**
Loads FastAPI and routes.

### 🔹 **routes.py**
Contains all API endpoints (e.g., organization create).

### 🔹 **models.py**
Defines the request body schema using Pydantic.

### 🔹 **database.py**
Creates MongoDB client and collections.

### 🔹 **config.py**
Stores database URI and JWT secret  
(**Real secrets should NOT be uploaded to GitHub**).

---

7. How It Works (Architecture)**

1. Client sends API request → `/org/create`  
2. Request is validated by Pydantic  
3. Password is hashed using bcrypt  
4. Data is stored in MongoDB  
5. Successful response returned  
6. Swagger UI is automatically generated  
7. Ngrok provides a public testing URL  

This architecture follows industry standards for cloud backend systems.

---

8. Things NOT to Upload to GitHub**

 MongoDB password  
 JWT_SECRET  
 ngrok token  
 `.env` file  
 Real connection string  

Instead use placeholders:
```
MONGO_URI = "YOUR_MONGO_URI_HERE"
```

---
9. Sample Test Using Python**

```python
import requests

BASE = "https://your-ngrok-url.ngrok-free.dev"

data = {
    "organization_name": "test_company",
    "email": "test@gmail.com",
    "password": "pass123"
}

res = requests.post(BASE + "/org/create", json=data)
print(res.json())
```

---
10. Conclusion**

This backend demonstrates:
- Cloud integration  
- Secure authentication handling  
- API development with FastAPI  
- Async database operations  
- Real-world modular backend architecture  



