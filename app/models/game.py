from pydantic import BaseModel


class Game(BaseModel):
    game_id: int
    name: str
    date: str
    teams: list
