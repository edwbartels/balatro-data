from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.database.main import Base
import uuid


class Planet(Base):
    __tablename__ = "planets"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    hand: Mapped[str] = mapped_column(String, nullable=False)
    chips: Mapped[int] = mapped_column(Integer, nullable=False)
    mult: Mapped[int] = mapped_column(Integer, nullable=False)
