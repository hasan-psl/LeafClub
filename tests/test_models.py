from datetime import date
from decimal import Decimal
import pytest
from sqlalchemy.exc import IntegrityError
from app.models import (
    Base,
    Club,
    ClubCategory,
    ClubStatus,
    Event,
    EventStatus,
    Member,
    MemberRole,
    MemberStatus,
    Transaction,
    TransactionType,
    User,
)


def test_schema_table_names():
    """Verify that all five tables match the specification exactly."""
    expected_tables = {"users", "clubs", "members", "events", "transactions"}
    actual_tables = set(Base.metadata.tables.keys())
    assert expected_tables == actual_tables


def test_schema_no_net_balance_column():
    """Verify that clubs table does not have a net balance column."""
    club_columns = {col.name for col in Base.metadata.tables["clubs"].columns}
    assert "net_balance" not in club_columns
    assert "balance" not in club_columns


def test_create_user(db_session):
    """Test user creation and persistence."""
    user = User(
        email="organizer@leafclub.edu",
        password_hash="hashed_secret_123",
        name="Club Organizer",
    )
    db_session.add(user)
    db_session.commit()

    assert user.id is not None
    assert user.email == "organizer@leafclub.edu"
    assert user.name == "Club Organizer"
    assert user.created_at is not None
    assert "organizer@leafclub.edu" in repr(user)


def test_user_email_unique_constraint(db_session):
    """Test that email uniqueness is enforced on users table."""
    user1 = User(
        email="duplicate@leafclub.edu",
        password_hash="hash1",
        name="First User",
    )
    db_session.add(user1)
    db_session.commit()

    user2 = User(
        email="duplicate@leafclub.edu",
        password_hash="hash2",
        name="Second User",
    )
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()
    db_session.rollback()


def test_create_club_and_relationships(db_session):
    """Test club creation with enums, dates, and user relationship."""
    user = User(
        email="clublead@leafclub.edu",
        password_hash="hash_pw",
        name="Club Leader",
    )
    db_session.add(user)
    db_session.commit()

    club = Club(
        user_id=user.id,
        name="Robotics Society",
        category=ClubCategory.TECH,
        status=ClubStatus.ACTIVE,
        founded_date=date(2024, 1, 15),
        description="University robotics and automation enthusiast club.",
    )
    db_session.add(club)
    db_session.commit()

    assert club.id is not None
    assert club.name == "Robotics Society"
    assert club.category == ClubCategory.TECH
    assert club.status == ClubStatus.ACTIVE
    assert club.user.id == user.id
    assert club in user.clubs
    assert "Robotics Society" in repr(club)


def test_create_member_and_relationship(db_session):
    """Test member creation with roles, status, and club relationship."""
    user = User(email="president@leafclub.edu", password_hash="pw")
    db_session.add(user)
    db_session.commit()

    club = Club(
        user_id=user.id,
        name="Debate Club",
        category=ClubCategory.ACADEMIC,
    )
    db_session.add(club)
    db_session.commit()

    member = Member(
        club_id=club.id,
        full_name="Jane Doe",
        student_id="STU-2026-001",
        email="jane.doe@student.leafclub.edu",
        phone="+1234567890",
        role=MemberRole.PRESIDENT,
        join_date=date(2026, 2, 1),
        status=MemberStatus.ACTIVE,
    )
    db_session.add(member)
    db_session.commit()

    assert member.id is not None
    assert member.full_name == "Jane Doe"
    assert member.role == MemberRole.PRESIDENT
    assert member.status == MemberStatus.ACTIVE
    assert member.club.id == club.id
    assert member in club.members
    assert "Jane Doe" in repr(member)


def test_create_event_and_budget_constraint(db_session):
    """Test event creation and budget constraint validation."""
    user = User(email="eventlead@leafclub.edu", password_hash="pw")
    db_session.add(user)
    db_session.commit()

    club = Club(
        user_id=user.id,
        name="Tech Club",
        category=ClubCategory.TECH,
    )
    db_session.add(club)
    db_session.commit()

    event = Event(
        club_id=club.id,
        title="Annual Hackathon 2026",
        description="48-hour student hackathon",
        event_date=date(2026, 11, 20),
        location="Student Center Main Hall",
        budget=Decimal("1500.50"),
        status=EventStatus.PLANNED,
    )
    db_session.add(event)
    db_session.commit()

    assert event.id is not None
    assert event.title == "Annual Hackathon 2026"
    assert event.budget == Decimal("1500.50")
    assert event.status == EventStatus.PLANNED
    assert event.club.id == club.id
    assert event in club.events
    assert "Annual Hackathon 2026" in repr(event)

    # Negative budget should fail check constraint
    invalid_event = Event(
        club_id=club.id,
        title="Invalid Budget Event",
        budget=Decimal("-100.00"),
    )
    db_session.add(invalid_event)
    with pytest.raises(IntegrityError):
        db_session.commit()
    db_session.rollback()


def test_create_transaction_and_amount_constraint(db_session):
    """Test transaction creation with Decimal amount and positive amount constraint."""
    user = User(email="treasurer_user@leafclub.edu", password_hash="pw")
    db_session.add(user)
    db_session.commit()

    club = Club(
        user_id=user.id,
        name="Music Society",
        category=ClubCategory.CULTURAL,
    )
    db_session.add(club)
    db_session.commit()

    event = Event(
        club_id=club.id,
        title="Spring Concert",
        budget=Decimal("500.00"),
    )
    db_session.add(event)
    db_session.commit()

    # Valid income transaction
    tx_income = Transaction(
        club_id=club.id,
        event_id=event.id,
        type=TransactionType.INCOME,
        amount=Decimal("350.75"),
        description="Ticket sales",
        transaction_date=date(2026, 3, 10),
    )
    db_session.add(tx_income)
    db_session.commit()

    assert tx_income.id is not None
    assert tx_income.type == TransactionType.INCOME
    assert tx_income.amount == Decimal("350.75")
    assert tx_income.event.id == event.id
    assert tx_income in event.transactions
    assert tx_income in club.transactions
    assert "350.75" in repr(tx_income)

    # Zero or negative amount should violate check constraint
    invalid_tx = Transaction(
        club_id=club.id,
        type=TransactionType.EXPENSE,
        amount=Decimal("0.00"),
        description="Zero amount test",
    )
    db_session.add(invalid_tx)
    with pytest.raises(IntegrityError):
        db_session.commit()
    db_session.rollback()


def test_event_deletion_sets_null_on_transaction(db_session):
    """Test that deleting an event sets event_id=NULL on transactions without deleting the transaction."""
    user = User(email="admin@leafclub.edu", password_hash="pw")
    db_session.add(user)
    db_session.commit()

    club = Club(user_id=user.id, name="Art Club", category=ClubCategory.CULTURAL)
    db_session.add(club)
    db_session.commit()

    event = Event(club_id=club.id, title="Art Exhibition")
    db_session.add(event)
    db_session.commit()

    tx = Transaction(
        club_id=club.id,
        event_id=event.id,
        type=TransactionType.EXPENSE,
        amount=Decimal("120.00"),
        description="Art supplies",
    )
    db_session.add(tx)
    db_session.commit()
    tx_id = tx.id

    # Delete event
    db_session.delete(event)
    db_session.commit()

    # Transaction should still exist with event_id=None
    refreshed_tx = db_session.get(Transaction, tx_id)
    assert refreshed_tx is not None
    assert refreshed_tx.event_id is None
    assert refreshed_tx.amount == Decimal("120.00")


def test_cascade_delete_club(db_session):
    """Test that deleting a club cascades to members, events, and transactions."""
    user = User(email="clubowner@leafclub.edu", password_hash="pw")
    db_session.add(user)
    db_session.commit()

    club = Club(user_id=user.id, name="Drama Society", category=ClubCategory.CULTURAL)
    db_session.add(club)
    db_session.commit()

    member = Member(club_id=club.id, full_name="Actor One")
    event = Event(club_id=club.id, title="Play Opening Night")
    db_session.add_all([member, event])
    db_session.commit()

    tx = Transaction(
        club_id=club.id,
        event_id=event.id,
        type=TransactionType.EXPENSE,
        amount=Decimal("200.00"),
    )
    db_session.add(tx)
    db_session.commit()

    member_id, event_id, tx_id = member.id, event.id, tx.id

    # Delete club
    db_session.delete(club)
    db_session.commit()

    # All related entities should be cascade deleted
    assert db_session.get(Member, member_id) is None
    assert db_session.get(Event, event_id) is None
    assert db_session.get(Transaction, tx_id) is None

