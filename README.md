# 🍃 LeafClub — University Club Management System

> [!WARNING]
> ### 🚧 Project Status: Active Work In Progress
> **LeafClub** is currently in early active development. There is **no stable, beta, or alpha release** available yet.
> 
> APIs, architecture, and database schemas are evolving rapidly. Please be patient as we build out the full backend system!

---

## 📌 Overview

**LeafClub** is a modern, full-stack **University Club Management System**. This repository currently contains the core backend REST API powering student club registrations, event management, membership tracking, financial transactions, and administrative management dashboards with full frontend yet to be developed.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.11+ | Modern, typed Python core |
| **Framework** | FastAPI | High-performance, async web application framework |
| **ORM** | SQLAlchemy 2.0 | Type-safe SQL toolkit and ORM |
| **Migrations** | Alembic | Database schema version control |
| **Database** | PostgreSQL | Enterprise-grade relational database |
| **Validation** | Pydantic v2 | Data serialization, schemas, and settings management |
| **Testing** | pytest | Automated test framework |

---

## 📂 Project Structure

```text
LeafClub/
├── app/
│   ├── api/          # Route handlers & endpoints (health, etc.)
│   ├── core/         # Settings configuration & database session manager
│   ├── models/       # SQLAlchemy ORM declarative models
│   └── main.py       # FastAPI application entry point
├── alembic/          # Database migration scripts & environments
├── tests/            # Automated test suite (pytest)
├── .env.example      # Example environment configuration template
├── .gitignore        # Version control ignore rules
├── pyproject.toml    # Project metadata & dependencies
├── requirements.txt  # Python package requirements
└── README.md         # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed locally:
* **Python 3.11+**
* **PostgreSQL** server (version 14+)

### 1. Clone & Environment Setup

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create your local `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Default configuration (`.env`):
```env
PROJECT_NAME=LeafClub
ENVIRONMENT=development
DEBUG=True
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/leafclub_db
```

### 4. Run Database Migrations

```bash
alembic upgrade head
```

### 5. Start Development Server

Launch the FastAPI live-reload server:

```bash
uvicorn app.main:app --reload
```

---

## 📍 API Reference

| Endpoint | Method | Description |
| :--- | :---: | :--- |
| `/` | `GET` | API welcome payload & quick links |
| `/health` | `GET` | Health check & system operational status |
| `/docs` | `GET` | Interactive Swagger UI documentation |
| `/redoc` | `GET` | ReDoc interactive API reference |

---

## 🧪 Testing

Run the full automated test suite using `pytest`:

```bash
pytest
```

---

## 📜 License & Copyright

This project is open-source software licensed under the **[GNU General Public License v3.0](LICENSE)**.

**Copyright (C) 2026 Khondokar Shazid Hassan (`hasan-psl`)**

* **GitHub Handle**: [`hasan-psl`](https://github.com/hasan-psl)
* **GitHub Email**: [`hasanimroz.personal@gmail.com`](mailto:hasanimroz.personal@gmail.com)
* **Official Email**: [`shazidhasan.official@gmail.com`](mailto:shazidhasan.official@gmail.com)
