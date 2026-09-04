# LeafClub Backend

LeafClub is a full-stack University Club Management System. This repository contains the backend REST API service powering student club registrations, event management, membership tracking, and administrative dashboards.

## Technology Stack

- **Python 3.11+**
- **FastAPI** - High-performance async web application framework
- **SQLAlchemy 2.0** - Python SQL Toolkit and Object Relational Mapper
- **Alembic** - Database migration tool for SQLAlchemy
- **PostgreSQL** - Relational database engine
- **Pydantic v2** - Data validation and settings management
- **pytest** - Test framework

---

## Local Backend Setup Prerequisites

- **Python 3.11+** installed on system
- **PostgreSQL** server instance running locally or accessible via network

---

## Getting Started

### 1. Environment Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example environment file and update database credentials if necessary:

```bash
cp .env.example .env
```

### 4. Running Database Migrations

```bash
alembic upgrade head
```

### 5. Running the Backend Server

Start the FastAPI development server with live reload:

```bash
uvicorn app.main:app --reload
```

The API will be available at:
- **API Base**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Health Check**: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
- **Interactive Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Running Tests

Execute the test suite using `pytest`:

```bash
pytest
```
