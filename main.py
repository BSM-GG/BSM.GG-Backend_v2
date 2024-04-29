from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controller.user.user_controller import user_controller
from domain.tables import Base
from database import engine

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(user_controller)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# /lol/league/v4/entries/by-riot/{encryptedSummonerId}
# 랭크 정보

# /lol/riot/v4/summoners/by-puuid/{encryptedPUUID}
# 유저 세부 정보

# /lol/match/v5/matches/by-puuid/{puuid}/ids
# 매치 정보

# import json
# import requests
#
# response = requests.get(...)
# json_data = json.loads(response.text)
