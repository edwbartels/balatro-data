from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from app.database.main import SessionLocal
from app.database.models.runs import Run
from app.database.models.rounds import Round, round_joker_instances
from app.database.models.jokers import JokerInstance, Joker


def update_db(data) -> None:
    # print(data.GAME)
    # print(data.cardAreas)
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
        if "rounds" not in existing_run.keys():
            return

    previous_run = session.query(Run).order_by(desc(Run.created_at)).first()

    if previous_run:
        if "rounds" in previous_run.keys():
            previous_run.completed = True

            joker_ids = (
                session.query(Joker.id)
                .join(JokerInstance, Joker.instances)
                .join(round_joker_instances)
                .join(Round)
                .filter(Round.run_id == previous_run.id)
                .distinct()
                .all()
            )

            for (joker_id,) in joker_ids:
                Joker.update_win_rate(session, joker_id)

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

    return


def new_round(data) -> None:
    session: Session = SessionLocal()
    hashed_id = data.GAME.pseudorandom.hashed_seed

    run_query = session.query(Run).filter(Run.hashed_seed == hashed_id)
    existing_run: Run | None = run_query.first()

    if not existing_run:
        print("Associated run not found, cannot create a new run if round != 0")
        return
    existing_run.win = data.GAME.won
    session.commit()

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

    print("default", data.cardAreas.jokers.cards)
    # usable = dict(data.cardAreas.jokers.get("cards"))
    # cards = data.cardAreas.jokers.cards
    # # print(cards)
    # # print(cards["1"])
    # for card in cards:
    #     print(cards[card])
    # # print(cards)
    # # for card in vars(data.cardAreas.jokers.cards):
    # #     print(data["cardAreas"]["jokers"]["cards"]["card"])
    # # print(data.cardAreas.jokers.cards)
    # # print(usable)
    cards = data.cardAreas.jokers.cards
    for card in cards:
        joker_instance = (
            session.query(JokerInstance)
            .filter(
                JokerInstance.joker_id == cards[card].joker_id,
                JokerInstance.edition == cards[card].edition.upper(),
                JokerInstance.persistence == cards[card].persistence.upper(),
                JokerInstance.is_rental == cards[card].is_rental,
            )
            .first()
        )
        # stmt = (
        #     select(round_joker_instances)
        #     .where(round_joker_instances.c.round_id == new_round.id)
        #     .where(round_joker_instances.c.joker_instance.id == joker_instance.id)
        # )
        # existing_in_round = session.execute(stmt)
        # print("joker_instance.id", joker_instance.id)
        existing_in_round = (
            session.query(round_joker_instances)
            .filter(
                round_joker_instances.c.round_id == new_round.id,
                round_joker_instances.c.joker_instance_id == joker_instance.id,
            )
            .first()
        )

        if existing_in_round:
            # print("????")
            # print(existing_in_round)
            # print(existing_in_round.count)
            # existing_in_round.count += 1
            # session.commit()
            session.execute(
                round_joker_instances.update()
                .where(
                    round_joker_instances.c.round_id == new_round.id,
                    round_joker_instances.c.joker_instance_id == joker_instance.id,
                )
                .values(count=round_joker_instances.c.count + 1)
            )
        else:
            session.execute(
                round_joker_instances.insert().values(
                    round_id=new_round.id, joker_instance_id=joker_instance.id
                )
            )
        session.commit()
    if new_round.round_number > 1:
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
