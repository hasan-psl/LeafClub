from datetime import date
from typing import TYPE_CHECKING, Optional
from sqlalchemy import Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from app.models.enums import MemberRole, MemberStatus

if TYPE_CHECKING:
    from app.models.club import Club


class Member(Base):
    """Member model representing a student enrolled in a club."""

    __tablename__ = "members"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    club_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("clubs.id", ondelete="CASCADE"), nullable=False, index=True
    )
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    student_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, index=True
    )
    email: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, index=True
    )
    phone: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    role: Mapped[MemberRole] = mapped_column(
        Enum(
            MemberRole,
            name="member_role",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        default=MemberRole.MEMBER,
        server_default=MemberRole.MEMBER.value,
    )
    join_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    status: Mapped[MemberStatus] = mapped_column(
        Enum(
            MemberStatus,
            name="member_status",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        default=MemberStatus.ACTIVE,
        server_default=MemberStatus.ACTIVE.value,
    )

    # Relationships
    club: Mapped["Club"] = relationship("Club", back_populates="members")

    def __repr__(self) -> str:
        return f"<Member(id={self.id}, full_name='{self.full_name}', role='{self.role}')>"
