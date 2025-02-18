import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from sqlalchemy import not_
from app.database.main import SessionLocal
from app.database.models import Run
from app.util.db_updates import (
    update_all_joker_win_rates,
    update_all_deck_stake_win_rates,
)


def remove_incomplete_runs() -> None:
    session = SessionLocal()
    try:
        incomplete_runs = session.query(Run).filter(not_(Run.complete)).all()

        count = len(incomplete_runs)

        for run in incomplete_runs:
            session.delete(run)

        print("Deletion step complete")

        update_all_joker_win_rates(session)
        update_all_deck_stake_win_rates(session)

        print("Win rate update step complete")

        session.commit()

        print(f"Successfully deleted {count} incomplete runs")

    except Exception as e:
        print(f"Error occured: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    remove_incomplete_runs()
