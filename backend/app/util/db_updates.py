import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from app.database.main import SessionLocal

from sqlalchemy.orm import Session
from dotenv import load_dotenv
from app.database.models.jokers import Joker
from app.database.models.runs import Run
from app.database.models.rounds import Round
from app.database.models.decks import Deck, DeckStakeStats

load_dotenv()
session: Session = SessionLocal()


def update_win(session, data):
    run = (
        session.query(Run)
        .filter(Run.hashed_seed == data.GAME.pseudorandom.hashed_seed)
        .first()
    )
    run.win = data.GAME.won
    Deck.update_win_rate(session, data.BACK.key)
    DeckStakeStats.update_stake_win_rates(session, data.BACK.key, data.GAME.stake)

    cards = data.cardAreas.jokers.cards
    for card in cards:
        Joker.update_win_rate(session, cards[card].joker_id)

    session.commit()


def update_all_joker_win_rates(session):
    joker_ids = session.query(Joker.id).all()

    for (joker_id,) in joker_ids:
        Joker.update_win_rate(session, joker_id)

    session.commit()


def set_all_runs_to_complete(session):
    runs = session.query(Run).all()
    for run in runs:
        run.complete = True

    session.commit()


def set_all_rounds_to_complete(session):
    rounds = session.query(Round).all()
    for round in rounds:
        round.complete = True

    session.commit()


def update_all_deck_stake_win_rates(session):
    decks = session.query(Deck).all()

    for deck in decks:
        for stake in range(1, 9):
            DeckStakeStats.update_stake_win_rates(session, deck.id, stake)
        Deck.update_win_rate(session, deck.id)


# def update_overall_deck_rates(session):
#     decks = session.query.all()


if __name__ == "__main__":
    # update_all_joker_win_rates(session)
    # set_all_runs_to_complete(session)
    # set_all_rounds_to_complete(session)
    update_all_deck_stake_win_rates(session)
