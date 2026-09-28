import enum


class ClubCategory(str, enum.Enum):
    """Enum for club category types."""

    CULTURAL = "cultural"
    SPORTS = "sports"
    ACADEMIC = "academic"
    TECH = "tech"
    OTHER = "other"


class ClubStatus(str, enum.Enum):
    """Enum for club operational status."""

    ACTIVE = "active"
    INACTIVE = "inactive"


class MemberRole(str, enum.Enum):
    """Enum for member roles within a club."""

    PRESIDENT = "president"
    VICE_PRESIDENT = "vice_president"
    TREASURER = "treasurer"
    MEMBER = "member"


class MemberStatus(str, enum.Enum):
    """Enum for member activity status."""

    ACTIVE = "active"
    INACTIVE = "inactive"


class EventStatus(str, enum.Enum):
    """Enum for event lifecycle status."""

    PLANNED = "planned"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TransactionType(str, enum.Enum):
    """Enum for financial transaction direction."""

    INCOME = "income"
    EXPENSE = "expense"
