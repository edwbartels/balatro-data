from sqlalchemy import select, desc, func
from sqlalchemy.orm import Session
from app.database.main import SessionLocal
from app.database.models.runs import Run
from app.database.models.decks import Deck, DeckStakeStats
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
    try:
        hashed_id = data.GAME.pseudorandom.hashed_seed

        # Check for existing run with this seed
        existing_run: Run | None = (
            session.query(Run).filter(Run.hashed_seed == hashed_id).first()
        )

        # Check for rounds. If none, assume existing == new and return without adding
        if existing_run and len(existing_run.rounds < 1):
            # if len(existing_run.rounds) < 1:
            return

        # Get previous run
        previous_run = (
            session.query(Run)
            .filter(not Run.complete)
            .order_by(desc(Run.created))
            .first()
        )

        if previous_run and previous_run.rounds > 0:
            # if len(previous_run.rounds) > 0:

            # Calculate and set max ante, toggle complete to true
            max_ante = (
                session.query(func.max(Round.ante))
                .filter(Round.run_id == previous_run.id)
                .scalar()
            )
            previous_run.complete = True
            previous_run.max_ante = max_ante

            # Update deck/stake win rates
            DeckStakeStats.update_stake_win_rates(
                session, previous_run.deck_id, previous_run.stake
            )
            Deck.update_win_rate(session, previous_run.deck_id)

            # Get Jokers and update win rates
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

        new_run = Run(
            hashed_seed=hashed_id,
            seed=data.GAME.pseudorandom.seed,
            stake=data.GAME.stake,
            deck_id=data.BACK.key,
        )

        session.add(new_run)
        session.commit()
        session.refresh(new_run)
    finally:
        session.close()


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
