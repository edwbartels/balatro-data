from sqlalchemy.orm import relationship
from .decks import Deck
from .runs import Run
from .rounds import Round
from .jokers import Joker, JokerInstance
from .joins import round_joker_instances

Joker.instances = relationship("JokerInstance", back_populates="base_joker")
JokerInstance.base_joker = relationship("Joker", back_populates="instances")


Round.joker_instances = relationship(
    "JokerInstance", secondary=round_joker_instances, back_populates="rounds"
)
JokerInstance.rounds = relationship(
    "Round", secondary=round_joker_instances, back_populates="joker_instances"
)
Deck.runs = relationship("Run", back_populates="deck")
Run.deck = relationship("Deck", back_populates="runs")
Run.rounds = relationship("Round", back_populates="run")
Round.run = relationship("Run", back_populates="rounds")
