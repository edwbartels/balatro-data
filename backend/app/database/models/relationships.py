from sqlalchemy import select, func
from sqlalchemy.orm import relationship, column_property
from .decks import Deck
from .runs import Run
from .rounds import Round
from .jokers import Joker, JokerInstance
from .joins import round_joker_instances


# Deck
Deck.runs = relationship("Run", back_populates="deck")
Deck.stake_stats = relationship("DeckStakeStats", backref="deck")

# Run
Run.deck = relationship("Deck", back_populates="runs")
Run.rounds = relationship("Round", back_populates="run", cascade="all, delete-orphan")
# Run.max_ante = column_property(
#     select(func.max(Round.ante)).where(Round.run_id == Run.id).scalar_subquery()
# )

# Round
Round.run = relationship("Run", back_populates="rounds")
Round.joker_instances = relationship(
    "JokerInstance",
    secondary=round_joker_instances,
    back_populates="rounds",
    cascade="all",
    passive_deletes=True,
)

# Joker
Joker.instances = relationship(
    "JokerInstance", back_populates="base_joker", cascade="all, delete-orphan"
)
JokerInstance.base_joker = relationship("Joker", back_populates="instances")
JokerInstance.rounds = relationship(
    "Round",
    secondary=round_joker_instances,
    back_populates="joker_instances",
    passive_deletes=True,
)
