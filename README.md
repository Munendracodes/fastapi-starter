# 🚀 FastAPI Starter Template

A clean and scalable FastAPI project structure designed for beginners and production-ready applications.

---

## 📌 Why This Project?

When starting new FastAPI projects, developers often:

- Repeat the same setup again and again
- Mix business logic with API routes
- Create messy, unscalable code

This template solves that by providing a **clean architecture** from day one.

---

## 📁 Project Structure

```
fastapi-starter/
│
├── app/
│   ├── main.py              # Entry point of the application
│   │
│   ├── api/                # API layer (routes)
│   │   └── v1/
│   │       ├── api.py
│   │       └── endpoints/
│   │           └── sample.py
│   │
│   ├── core/               # Core configs (settings, security)
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   └── security.py
│   │
│   ├── db/                 # Database setup
│   │   ├── session.py
│   │   └── base.py
│   │
│   ├── models/             # Database models
│   ├── schemas/            # Pydantic schemas
│   ├── services/           # Business logic
│   └── utils/              # Helper functions
│
├── tests/                  # Test cases
├── .env                    # Environment variables
├── requirements.txt        # Dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/<your-username>/fastapi-starter.git
cd fastapi-starter
```

---

### 2. Create Virtual Environment

#### Windows

```
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

```
cp .env.example .env
```

(For Windows)

```
copy .env.example .env
```

---

### 5. Run the Application

```
uvicorn app.main:app --reload
```

---

## 🌐 API Endpoints

| Method | Endpoint          | Description  |
| ------ | ----------------- | ------------ |
| GET    | `/`               | Health check |
| GET    | `/api/v1/sample/` | Sample API   |

---

## 📖 API Documentation

FastAPI provides built-in docs:

- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

---

## 🧪 Running Tests

```
pytest
```

---

## 🧠 Architecture Explanation

### 1. API Layer (`api/`)

Handles HTTP requests and responses.

### 2. Service Layer (`services/`)

Contains business logic.

### 3. Schema Layer (`schemas/`)

Validates request and response data.

### 4. Model Layer (`models/`)

Defines database structure.

---

## ⚠️ Best Practices

- Do NOT write business logic inside API routes
- Always use services for logic
- Keep configs in `.env`
- Write tests for critical features

---

## 🚀 Future Improvements

- Add JWT Authentication
- Add Database migrations (Alembic)
- Add Docker support
- Add logging system

---

## 👨‍💻 Author

Your Name

---

## ⭐ Contribute

Feel free to fork and improve this template!
