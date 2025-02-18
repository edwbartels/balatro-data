from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:default@localhost:5432/balatro"
)
SCHEMA = os.getenv("SCHEMA", None)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData(schema=SCHEMA) if SCHEMA else None
Base = declarative_base(metadata=metadata)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    from app.database.models.jokers import Joker
    from app.database.models.bosses import Boss
    from app.database.models.decks import Deck, DeckStakeStats
    from app.database.models.editions import Edition
    from app.database.models.packs import Pack
    from app.database.models.planets import Planet
    from app.database.models.seals import Seal
    from app.database.models.spectrals import Spectral
    from app.database.models.tarots import Tarot
    from app.database.models.vouchers import Voucher
    from app.database.models.runs import Run
    from app.database.models.rounds import Round
    from app.database.models.joins import round_joker_instances
    from app.database.models import relationships

    Base.metadata.create_all(bind=engine)


def drop_tables():
    from app.database.models.jokers import Joker
    from app.database.models.bosses import Boss
    from app.database.models.decks import Deck
    from app.database.models.editions import Edition
    from app.database.models.packs import Pack
    from app.database.models.planets import Planet
    from app.database.models.seals import Seal
    from app.database.models.spectrals import Spectral
    from app.database.models.tarots import Tarot
    from app.database.models.vouchers import Voucher
    from app.database.models.runs import Run
    from app.database.models.rounds import Round
    from app.database.models.joins import round_joker_instances
    from app.database.models import relationships

    Base.metadata.drop_all(bind=engine)
