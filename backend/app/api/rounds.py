from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query
from app.database.main import get_db
from app.database.models import Round, Run

router = APIRouter(prefix="/rounds", tags=["rounds"])


@router.get("/")
def get_all_runs(db: Session = Depends(get_db)):
    rounds = db.query(Round).all()

    return rounds


@router.get("/{round_id}")
def get_round_by_id(round_id: UUID, db: Session = Depends(get_db)):
    round_instance = db.query(Round).filter(Round.id == round_id).first()

    return round_instance


@router.get("/rn/{run_id}")
def get_rounds_by_run_id(run_id: UUID, db: Session = Depends(get_db)):
    rounds = db.query(Round).filter(Round.run_id == run_id).all()

    return rounds


@router.get("/u?{user_id}")
def get_rounds_by_user_id(user_id: str, db: Session = Depends(get_db)):
    rounds = db.query(Run).filter(Run.user_id == user_id).all()

    return rounds
