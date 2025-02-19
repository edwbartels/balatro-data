from pydantic import BaseModel
from datetime import datetime


class StakeStats(BaseModel):
    win_rate: float
    win_rate_updated_at: datetime
    avg_max_ante: float


class DeckResponse(BaseModel):
    name: str
    win_rate: float
    win_rate_updated_at: datetime
    id: str
    desc: str
    avg_max_ante: float
    stakes: dict[int, StakeStats]
