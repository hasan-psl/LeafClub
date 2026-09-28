from datetime import date, datetime
from typing import TYPE_CHECKING, List, Optional
from sqlalchemy import Date, DateTime, Enum, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from app.models.enums import ClubCategory, ClubStatus

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.member import Member
    from app.models.event import Event
    from app.models.transaction import Transaction


class Club(Base):
    """Club model representing a student club or society."""

    __tablename__ = "clubs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    category: Mapped[ClubCategory] = mapped_column(
        Enum(
            ClubCategory,
            name="club_category",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
    )
    status: Mapped[ClubStatus] = mapped_column(
        Enum(
            ClubStatus,
            name="club_status",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        default=ClubStatus.ACTIVE,
        server_default=ClubStatus.ACTIVE.value,
    )
    founded_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="clubs")
    members: Mapped[List["Member"]] = relationship(
        "Member", back_populates="club", cascade="all, delete-orphan"
    )
    events: Mapped[List["Event"]] = relationship(
        "Event", back_populates="club", cascade="all, delete-orphan"
    )
    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction", back_populates="club", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Club(id={self.id}, name='{self.name}', category='{self.category}')>"
