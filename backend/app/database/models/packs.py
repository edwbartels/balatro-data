from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.database.main import Base
import uuid
from typing import Literal


class Pack(Base):
    __tablename__ = "packs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    cat: Mapped[Literal["standard", "arcana", "celestial", "buffoon"]] = mapped_column(
        String, nullable=False
    )
    family: Mapped[Literal["normal", "jumbo", "mega"]] = mapped_column(
        String, nullable=False
    )
    size: Mapped[int] = mapped_column(Integer, nullable=False)
    selections: Mapped[int] = mapped_column(Integer, nullable=False)
