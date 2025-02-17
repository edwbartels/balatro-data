from fastapi import FastAPI, APIRouter
from app.api import rounds, runs, jokers

import os

app = FastAPI()

api_router = APIRouter(prefix="/api")

api_router.include_router(runs.router)
api_router.include_router(rounds.router)
api_router.include_router(jokers.router)

app.include_router(api_router)
