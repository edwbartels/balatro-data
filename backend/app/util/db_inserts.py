from sqlalchemy.orm import Session
from app.database.main import SessionLocal
from app.database.models.runs import Run
from app.database.models.rounds import Round


def update_db(data) -> None:
    print(data.GAME)
    if data.GAME.round == 0:
        new_run(data)
    else:
        new_round(data)


def new_run(data) -> None:
    session: Session = SessionLocal()
    hashed_id = data.GAME.pseudorandom.hashed_seed

    existing_run: Run | None = (
        session.query(Run).filter(Run.hashed_seed == hashed_id).first()
    )

    if existing_run:
        return

    deck_id = data.BACK.key
    # deck = session.query(Deck).filter(Deck.id == deck_id).first()
    new_run = Run(
        hashed_seed=hashed_id,
        seed=data.GAME.pseudorandom.seed,
        stake=data.GAME.stake,
        deck_id=deck_id,
    )

    session.add(new_run)
    session.commit()
    session.refresh(new_run)
    print(new_run)

    return


def new_round(data) -> None:
    session: Session = SessionLocal()
    hashed_id = data.GAME.pseudorandom.hashed_seed

    run_query = session.query(Run).filter(Run.hashed_seed == hashed_id)
    existing_run: Run | None = run_query.first()

    if not existing_run:
        print("Associated run not found, cannot create a new run if round != 0")
        return

    print(existing_run)
    if existing_run.rounds:
        for n in existing_run.rounds:
            if n.round_number == data.GAME.round:
                print("Round already exists")
                return

    blind = 0
    if data.BLIND.boss:
        blind = 3
    else:
        if data.BLIND.config_blind == "bl_big":
            blind = 2
        if data.BLIND.config_blind == "bl_small":
            blind = 1

    new_round = Round(
        run_id=existing_run.id,
        ante=data.GAME.round_resets.blind_ante,
        blind=blind,
        round_number=data.GAME.round,
    )
    session.add(new_round)
    session.commit()
    session.refresh(new_round)
    previous_round = (
        session.query(Round)
        .filter(
            Round.run_id == existing_run.id,
            Round.round_number == new_round.round_number - 1,
        )
        .first()
    )
    previous_round.complete = True
    previous_round.win = True
    session.commit()
