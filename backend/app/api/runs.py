from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query
from app.database.main import get_db
from app.database.models import Run

router = APIRouter(prefix="/runs", tags=["runs"])


@router.get("/")
def get_all_runs(db: Session = Depends(get_db)):
    runs = db.query(Run).all()

    return runs


@router.get("/{run_id}")
def get_run_by_id(run_id: UUID, db: Session = Depends(get_db)):
    run = db.query(Run).filter(Run.id == run_id).first()

    return run


# @router.get("/u?{user_id}")
# def get_runs_by_user_id(user_id: str, db: Session = Depends(get_db)):
#     runs = db.query(Run).filter(Run.user_id == user_id).all()

#     return runs
