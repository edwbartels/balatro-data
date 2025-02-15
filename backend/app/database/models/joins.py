from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.database.main import Base

round_joker_instances = Table(
    "round_joker_instances",
    Base.metadata,
    Column("round_id", UUID(as_uuid=True), ForeignKey("rounds.id"), primary_key=True),
    Column(
        "joker_instance_id",
        UUID(as_uuid=True),
        ForeignKey("joker_instances.id"),
        primary_key=True,
    ),
    Column("count", Integer, nullable=False, default=1),
)
