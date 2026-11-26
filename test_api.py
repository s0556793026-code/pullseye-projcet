from fastapi import FastAPI
import db
from pydantic import BaseModel
from random import choice
from data import new_secret_code

app = FastAPI()


class Game(BaseModel):
    secret_code: str = new_secret_code()
    attempts_used : int = 0
    status: str = 'in_progress'


@app.post("/games", status_code=201)
def new_game(game: Game):
    db.add_game(game.secret_code, game.attempts_used, game.status)


@app.post("/games/{game_id}/guesses")
def add_guess(gane_id: int, guesses: list[str]):
    db.add_guesses(game_id, guess)