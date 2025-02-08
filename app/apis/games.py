"""Games"""
from fastapi import APIRouter

from app.models.game import Game

router = APIRouter()


@router.get("/games", response_model=Game)
def get_games():
    return {"games": ["Game 1", "Game 2", "Game 3"]}


@router.get("/games/{game_id}", response_model=Game)
def get_game(game_id: int):
    return Game(game_id=game_id, name=f"Game {game_id}", date="2025-02-08", teams=["Team A", "Team B"])
