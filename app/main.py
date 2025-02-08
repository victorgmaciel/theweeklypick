from fastapi import FastAPI
from app.apis import games, leaderboard


app = FastAPI()

# Include the endpoints from other files
app.include_router(games.router)
app.include_router(leaderboard.router)
