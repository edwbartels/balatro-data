from sqlalchemy import (
    Integer,
    String,
    Enum,
    ForeignKey,
    Boolean,
    UniqueConstraint,
    Float,
    DateTime,
    func,
    case,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database.main import Base
from app.database.models.joins import round_joker_instances
from app.database.models.rounds import Round
from app.database.models.runs import Run
import uuid
import enum
from datetime import datetime


class JokerEdition(enum.Enum):
    STANDARD = "standard"
    FOIL = "foil"
    HOLO = "holographic"
    POLYCHROME = "polychrome"
    NEGATIVE = "negative"


class JokerPersistence(enum.Enum):
    STANDARD = "standard"
    ETERNAL = "eternal"
    PERISHABLE = "perishable"


class Joker(Base):
    __tablename__ = "jokers"

    id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(String, nullable=False)
    rarity: Mapped[int] = mapped_column(Integer, nullable=False)
    desc: Mapped[str] = mapped_column(String, nullable=False)
    win_rate: Mapped[float] = mapped_column(Float, server_default=text("0.0"))
    win_rate_updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )

    @classmethod
    def update_win_rate(cls, session, joker_id):
        result = (
            session.query(
                func.count(func.distinct(case((Run.win == True, Run.id)))),
                func.count(func.distinct(Run.id)),
            )
            .join(JokerInstance, cls.instances)
            .join(round_joker_instances)
            .join(Round)
            .join(Run)
            .filter(cls.id == joker_id)
            .first()
        )

        wins, total = result
        win_rate = wins / total if total > 0 else 0.0

        session.query(cls).filter(cls.id == joker_id).update(
            {"win_rate": win_rate, "win_rate_updated_at": func.now()}
        )
        session.commit()

    # instances = relationship("JokerInstance", back_populates="base_joker")


class JokerInstance(Base):
    __tablename__ = "joker_instances"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    joker_id: Mapped[str] = mapped_column(
        String, ForeignKey("jokers.id"), nullable=False
    )
    edition: Mapped[JokerEdition] = mapped_column(Enum(JokerEdition), nullable=False)
    persistence: Mapped[JokerPersistence] = mapped_column(
        Enum(JokerPersistence), nullable=False
    )
    is_rental: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    # base_joker = relationship("Joker", back_populates="instances")
    # rounds = relationship(
    #     "Round", secondary=round_joker_instances, back_populates="joker_instances"
    # )

    __table_args__ = (
        UniqueConstraint(
            "joker_id",
            "edition",
            "persistence",
            "is_rental",
            name="unique_joker_instance",
        ),
    )

    @property
    def edition_display(self) -> str:
        return self.edition.name.title()

    @property
    def persistence_display(self) -> str:
        return self.persistence.name.title()
