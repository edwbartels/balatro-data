import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from app.database.main import SessionLocal

from app.seed.joker_list import (
    jokers,
    create_all_joker_instances,
    verify_seed,
)
from app.seed.boss_list import bosses
from app.seed.deck_list import decks
from app.seed.edition_list import editions
from app.seed.enhancement_list import enhancements
from app.seed.pack_list import packs
from app.seed.planet_list import planets
from app.seed.seal_list import seals
from app.seed.spectral_list import spectrals
from app.seed.tarot_list import tarots
from app.seed.voucher_list import vouchers

from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()


def seed_data() -> None:
    session: Session = SessionLocal()
    try:
        session.add_all(jokers)
        session.commit()
        print(f"Seeded {len(jokers)} jokers.")
        create_all_joker_instances(session)
        session.commit()
        verify_seed(session)
        session.add_all(bosses)
        session.commit()
        print(f"Seeded {len(bosses)} bosses.")
        session.add_all(decks)
        session.commit()
        print(f"Seeded {len(decks)} decks.")
        session.add_all(editions)
        session.commit()
        print(f"Seeded {len(editions)} editions.")
        session.add_all(enhancements)
        session.commit()
        print(f"Seeded {len(enhancements)} enhancements.")
        session.add_all(packs)
        session.commit()
        print(f"Seeded {len(packs)} packs.")
        session.add_all(planets)
        session.commit()
        print(f"Seeded {len(planets)} planets.")
        session.add_all(seals)
        session.commit()
        print(f"Seeded {len(seals)} seals.")
        session.add_all(spectrals)
        session.commit()
        print(f"Seeded {len(spectrals)} spectrals.")
        session.add_all(tarots)
        session.commit()
        print(f"Seeded {len(tarots)} tarots.")
        session.add_all(vouchers)
        session.commit()
        print(f"Seeded {len(vouchers)} vouchers.")

        print(f"Database seeded successfully")
    except Exception as e:
        session.rollback()
        print(f"Failed to seed data: {str(e)}")
    finally:
        session.close()


if __name__ == "__main__":
    seed_data()
