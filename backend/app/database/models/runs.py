from sqlalchemy import ForeignKey, Integer, Boolean, Float, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.database.main import Base
from app.database.models.mixins import TimestampMixin
import uuid


class Run(Base, TimestampMixin):
    __tablename__ = "runs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    deck_id: Mapped[str] = mapped_column(String, ForeignKey("decks.id"), nullable=False)

    hashed_seed: Mapped[float] = mapped_column(
        Float, index=True, nullable=False, unique=True
    )
    seed: Mapped[str] = mapped_column(String, nullable=False)
    complete: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    win: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    stake: Mapped[int] = mapped_column(Integer, nullable=False)

    # rounds = relationship("Round", back_populates="run")
    # deck = relationship("Deck", back_populates="runs")
