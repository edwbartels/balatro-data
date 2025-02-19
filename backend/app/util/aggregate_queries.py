from sqlalchemy import func
from app.database.models.runs import Run
from app.database.models.decks import Deck


def get_avg_max_ante_for_deck(session, deck_id):
    return (
        session.query(func.av(Run.max_ante))
        .filter(Run.deck_id == deck_id)
        .filter(Run.complete)
        .scalar()
    )


def get_all_deck_avg_max_antes(session):
    return (
        session.query(Deck.id, Deck.name, func.avg(Run.max_ante).label("avg_max_ante"))
        .join(Run)
        .filter(Run.complete)
        .group_by(Deck.id, Deck.name)
        .all()
    )
