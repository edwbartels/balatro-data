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

load_dotenv()
session: Session = SessionLocal()


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


if __name__ == "__main__":
    # update_all_joker_win_rates(session)
    # set_all_runs_to_complete(session)
    set_all_rounds_to_complete(session)
