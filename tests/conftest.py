import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from app.main import app
from app.models import Base


# ---------------------------------------------------------------------------
# API client fixture
# ---------------------------------------------------------------------------

@pytest.fixture
def client():
    """Pytest fixture providing a TestClient for testing API endpoints."""
    with TestClient(app) as test_client:
        yield test_client


# ---------------------------------------------------------------------------
# In-memory SQLite database fixture for model tests
# ---------------------------------------------------------------------------

@pytest.fixture
def db_session():
    """
    Pytest fixture providing a transactional SQLAlchemy Session backed by an
    in-memory SQLite database.  Each test gets a fresh schema and a session
    that is rolled back after the test completes so tests are fully isolated.

    SQLite note: foreign-key enforcement is disabled by default.  The fixture
    enables it via a PRAGMA so that FK-cascade / SET-NULL behaviour is tested
    correctly.
    """
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
    )

    # Enable FK enforcement for SQLite
    @event.listens_for(engine, "connect")
    def set_sqlite_pragma(dbapi_conn, _connection_record):
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    Base.metadata.create_all(engine)
    TestingSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

    session: Session = TestingSession()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)
        engine.dispose()
