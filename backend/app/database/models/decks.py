from http import server
from sqlalchemy import String, Float, text, func, DateTime, case, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.database.main import Base
from app.database.models.runs import Run
import uuid
from datetime import datetime


class Deck(Base):
    __tablename__ = "decks"

    id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    desc: Mapped[str] = mapped_column(String, nullable=False)
    win_rate: Mapped[float] = mapped_column(Float, server_default=text("0.0"))
    win_rate_updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    # runs = relationship("Run", back_populates="deck")

    @property
    def stakes(self):
        stakes_dict = {}

        for stat in self.stake_stats:
            stakes_dict[stat.stake] = {
                "win_rate": stat.win_rate,
                "win_rate_updated_at": stat.win_rate_updated_at,
            }
        return stakes_dict

    @classmethod
    def update_win_rate(cls, session, deck_id):
        result = (
            session.query(
                func.count(
                    func.distinct(case((Run.win == True, Run.id)))
                ),  # Count wins
                func.count(func.distinct(Run.id)),  # Count total
            )
            .filter(Run.deck_id == deck_id)
            .first()
        )

        wins, total = result
        win_rate = wins / total if total > 0 else 0.0

        session.query(cls).filter(cls.id == deck_id).update(
            {"win_rate": win_rate, "win_rate_updated_at": func.now()}
        )

        session.commit()

    def get_win_rate_for_stake(self, stake):
        stats = next((s for s in self.stake_stats if s.stake == stake), None)
        return stats.win_rate if stats else 0.0


class DeckStakeStats(Base):
    __tablename__ = "deck_stake_stats"

    deck_id: Mapped[str] = mapped_column(
        String, ForeignKey("decks.id"), primary_key=True
    )
    stake: Mapped[int] = mapped_column(Integer, primary_key=True)
    win_rate: Mapped[float] = mapped_column(Float, server_default=text("0.0"))
    win_rate_updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )

    def get_stake_stats(self, session, stake=None):
        query = session.query(DeckStakeStats).filter_by(deck_id=self.id)

        if stake:
            return query.filter_by(stake=stake).first()
        return query.all()

    @classmethod
    def update_stake_win_rates(cls, session, deck_id, stake):
        result = (
            session.query(
                func.count(func.distinct(case((Run.win == True, Run.id)))),
                func.count(func.distinct(Run.id)),
            )
            .filter(Run.deck_id == deck_id, Run.stake == stake)
            .first()
        )

        wins, total = result
        win_rate = wins / total if total > 0 else 0.0

        stats = (
            session.query(DeckStakeStats)
            .filter_by(deck_id=deck_id, stake=stake)
            .first()
        )

        if stats:
            stats.win_rate = win_rate
            stats.win_rate_updated_at = func.now()
        else:
            stats = DeckStakeStats(
                deck_id=deck_id,
                stake=stake,
                win_rate=win_rate,
                win_rate_updated_at=func.now(),
            )
            session.add(stats)

        session.commit()
