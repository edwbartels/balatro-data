from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.database.main import Base
import uuid


class Deck(Base):
    __tablename__ = "decks"

    id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    desc: Mapped[str] = mapped_column(String, nullable=False)
    # runs = relationship("Run", back_populates="deck")
