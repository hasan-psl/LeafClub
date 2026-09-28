from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING, List, Optional
from sqlalchemy import (
    CheckConstraint,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from app.models.enums import EventStatus

if TYPE_CHECKING:
    from app.models.club import Club
    from app.models.transaction import Transaction


class Event(Base):
    """Event model representing an activity organized by a club."""

    __tablename__ = "events"
    __table_args__ = (
        CheckConstraint("budget >= 0", name="ck_events_budget_non_negative"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    club_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("clubs.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    event_date: Mapped[Optional[date]] = mapped_column(
        Date, nullable=True, index=True
    )
    location: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    budget: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(12, 2), nullable=True
    )
    status: Mapped[EventStatus] = mapped_column(
        Enum(
            EventStatus,
            name="event_status",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        default=EventStatus.PLANNED,
        server_default=EventStatus.PLANNED.value,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships
    club: Mapped["Club"] = relationship("Club", back_populates="events")
    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction", back_populates="event"
    )

    def __repr__(self) -> str:
        return f"<Event(id={self.id}, title='{self.title}', status='{self.status}')>"

