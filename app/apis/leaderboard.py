"""Leaderboard"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/leaderboard")
def get_leaderboard():
    return {"leaderboard": [
        {"user": "User1", "wins": 10},
        {"user": "User2", "wins": 8}
    ]}
