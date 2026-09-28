# 🍃 LeafClub — University Club Management System

> [!WARNING]
> ### 🚧 Project Status: Active Work In Progress
> **LeafClub** is currently in early active development. There is **no stable, beta, or alpha release** available yet.
>
> APIs, architecture, and database schemas are evolving rapidly. Please be patient as we build out the full backend system!

---

## 📌 Overview

**LeafClub** is a modern, full-stack **University Club Management System**. This repository currently contains the core backend REST API powering student club registrations, event management, membership tracking, and financial transaction records — with the full frontend yet to be developed.

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
| **Testing** | pytest + SQLite | Automated test suite (no external DB required) |

---

## 🗄️ Data Model

The database consists of five tables with the following relationships:

```
users (1) ──── (N) clubs (1) ──── (N) members
                          │
                          └──── (N) events (1) ──── (N) transactions
                          │
                          └──── (N) transactions
```

| Table | Description |
| :--- | :--- |
| `users` | System accounts that own and manage clubs |
| `clubs` | Student clubs with category, status, and founding date |
| `members` | Students enrolled in a club with roles and status |
| `events` | Activities organized by a club with optional budget |
| `transactions` | Financial income/expense records linked to a club and optionally an event |

---

## 📂 Project Structure

```text
LeafClub/
├── app/
│   ├── api/          # Route handlers & endpoints (health, etc.)
│   ├── core/         # Settings configuration & database session manager
│   ├── models/       # SQLAlchemy ORM declarative models
│   │   ├── base.py         # DeclarativeBase
│   │   ├── enums.py        # All Enum types (ClubCategory, EventStatus, …)
│   │   ├── user.py
│   │   ├── club.py
│   │   ├── member.py
│   │   ├── event.py
│   │   └── transaction.py
│   └── main.py       # FastAPI application entry point
├── alembic/          # Database migration scripts & environments
├── tests/            # Automated test suite (pytest)
│   ├── conftest.py         # Shared fixtures (client, db_session)
│   ├── test_health.py      # API endpoint smoke tests
│   └── test_models.py      # ORM model & constraint tests
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
* **Python 3.11+** (system build with SQLite support for tests)
* **PostgreSQL** server (version 14+) for running the application

### 1. Clone & Environment Setup

```bash
# Clone the repository
git clone https://github.com/hasan-psl/LeafClub.git
cd LeafClub

# Create a virtual environment using the system Python
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

The test suite runs entirely against an **in-memory SQLite database** — no PostgreSQL setup is required.

> [!NOTE]
> SQLite foreign-key enforcement is enabled via `PRAGMA foreign_keys=ON` in the test fixture, so cascade deletes and `SET NULL` behaviours are fully exercised.

Run the full automated test suite:

```bash
pytest
```

Or with verbose output:

```bash
pytest -v
```

### Test Coverage

| File | Tests | Description |
| :--- | :---: | :--- |
| `test_health.py` | 2 | API endpoint smoke tests (`/` and `/health`) |
| `test_models.py` | 10 | ORM model CRUD, uniqueness, check constraints, cascade deletes |

> [!IMPORTANT]
> **Python build requirement**: Your Python installation must be compiled with SQLite support (`_sqlite3` module). Standard distro-packaged Python builds (e.g. `/usr/bin/python3`) include this by default. If you use a custom-built or tool-managed Python that lacks `_sqlite3`, recreate the virtual environment with your system Python.

---

## 📜 License & Copyright

This project is open-source software licensed under the **[GNU General Public License v3.0](LICENSE)**.

**Copyright (C) 2026 Khondokar Shazid Hassan (`hasan-psl`)**

* **GitHub Handle**: [`hasan-psl`](https://github.com/hasan-psl)
* **GitHub Email**: [`hasanimroz.personal@gmail.com`](mailto:hasanimroz.personal@gmail.com)
* **Official Email**: [`shazidhasan.official@gmail.com`](mailto:shazidhasan.official@gmail.com)
