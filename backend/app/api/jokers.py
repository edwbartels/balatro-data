from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query
from app.database.main import get_db
from app.database.models import Joker, JokerInstance, Round, Run, round_joker_instances

router = APIRouter(prefix="/jokers", tags=["jokers"])


@router.get("/")
def get_all_jokers(db: Session = Depends(get_db)):
    jokers = db.query(Joker).all()

    return jokers


@router.get("/{joker_id}")
def get_joker_by_id(joker_id: str, db: Session = Depends(get_db)):
    joker = db.query(Joker).filter(Joker.id == joker_id).first()

    return joker


@router.get("/rn/{run_id}")
def get_jokers_by_run(run_id: UUID, db: Session = Depends(get_db)):
    all_jokers = (
        db.query(JokerInstance)
        .join(round_joker_instances)
        .join(Round)
        .filter(Round.run_id == run_id)
        .distinct()
        .all()
    )
    final_jokers = (
        db.query(JokerInstance)
        .join(round_joker_instances)
        .join(Round)
        .filter(
            Round.run_id == run_id,
            Round.round_number
            == (db.query(func.max(Round.round_number)).filter(Round.run_id == run_id)),
        )
        .all()
    )

    return {"all jokers": all_jokers, "final_jokers": final_jokers}


@router.get("/rd/{round_id}")
def get_jokers_by_round(round_id: UUID, db: Session = Depends(get_db)):
    jokers = (
        db.query(JokerInstance)
        .join(round_joker_instances)
        .join(Round)
        .filter(Round.id == round_id)
        .distinct()
        .all()
    )

    return jokers
