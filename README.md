# 🐞 Bug Tracker

A simple **Bug Tracker** web application built with **FastAPI**, **SQLAlchemy**, and **Uvicorn**.  
Easily track, create, update, and manage bugs for any project.

---

## 🚀 Features

- Create, read, update, and delete (CRUD) bug reports
- Track bug status: `Open`, `In Progress`, `Resolved`, `Closed`
- Simple API with JSON endpoints
- Lightweight and fast with **FastAPI**
- Database support with **SQLAlchemy**

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI |
| ORM | SQLAlchemy |
| ASGI Server | Uvicorn |
| Database | SQLite (default, can be changed to PostgreSQL/MySQL) |

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/bug-tracker.git
cd bug-tracker
```



Create a virtual environment and activate it:

### Windows
```
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

⚡ Running the Project:

Start the FastAPI server with Uvicorn:
```
uvicorn main:app --reload
```

Open your browser and go to:
```
http://127.0.0.1:8000/docs
```

You will see the interactive Swagger API documentation.




