from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query
from app.database.main import get_db
from app.database.models import Deck
from app.api.schema import StakeStats, DeckResponse
from app.util.response_format import format_deck_response

router = APIRouter(prefix="/decks", tags=["decks"])


@router.get("/", response_model=dict[str, DeckResponse])
def get_all_decks(db: Session = Depends(get_db)):
    decks = db.query(Deck).all()
    result = {}
    for deck in decks:
        result[deck.id] = deck

    return result


@router.get("/{deck_id}", response_model=DeckResponse)
def get_deck_by_id(deck_id: str, db: Session = Depends(get_db)):
    deck = db.query(Deck).filter(Deck.id == deck_id).first()

    return deck
