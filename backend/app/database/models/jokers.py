from sqlalchemy import Integer, String, Enum, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database.main import Base
from app.database.models.joins import round_joker_instances
from app.database.models.rounds import Round
import uuid
import enum


class JokerEdition(enum.Enum):
    STANDARD = "standard"
    FOIL = "foil"
    HOLO = "holographic"
    POLY = "polychrome"
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
