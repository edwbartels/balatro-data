from sqlalchemy.orm import Session

# from sqlalchemy.orm.query import Query
from app.database.main import SessionLocal
from app.database.models.runs import Run


def process_change(json_file) -> None:
    session: Session = SessionLocal()
    hashed_id = json_file["GAME"]["pseudorandom"]["hashed_seed"]

    existing_run: Run | None = (
        session.query(Run).filter(Run.hashed_seed == hashed_id).first()
    )

    if existing_run:
        return

    new_run = Run(hashed_seed=hashed_id, seed=json_file["GAME"]["pseudorandom"]["seed"])

    session.add(new_run)
    session.commit()
    session.refresh(new_run)
    print(new_run)

    return
