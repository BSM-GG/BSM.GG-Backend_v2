from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.controller.riot.riot_controller import riot_controller
from app.controller.user.user_controller import user_controller
from app.domain.restapi.tables import Base
from app.database import engine
from app.domain.graphql.schema import graphql_app


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



@app.get("/hello/{name}", description="테스트 api")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(user_controller)
app.include_router(riot_controller)
app.include_router(graphql_app, prefix="/graphql")

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

# 1714444000
# 1704855600
# 1709313179601