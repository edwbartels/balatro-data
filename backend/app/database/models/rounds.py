from sqlalchemy import Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database.main import Base
from app.database.models.mixins import TimestampMixin
from app.database.models.joins import round_joker_instances
import uuid


class Round(Base, TimestampMixin):
    __tablename__ = "rounds"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    run_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("runs.id"),
        index=True,
    )
    ante: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    blind: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    complete: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    win: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    round_number: Mapped[int] = mapped_column(Integer, nullable=False)
    # joker_instances = relationship(
    #     "JokerInstance", secondary=round_joker_instances, back_populates="rounds"
    # )

    # run = relationship("Run", back_populates="rounds")
