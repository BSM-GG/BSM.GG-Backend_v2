from fastapi import APIRouter, Header

from app.controller.riot.model.riot_model import SummonerModel
from app.service.riot.riot_service import RiotService

riot_controller = APIRouter(prefix="/api/riot", tags=["riot"])
riot_service = RiotService()


@riot_controller.post("/summoner", description="소환사 등록")
async def assign_summoner(
        summoner: SummonerModel,
        token: str = Header(default=None),
) -> None:
    if token == "": return
    await riot_service.assign_summoner(token, summoner.game_name, summoner.tag_line)


@riot_controller.post("/match", description="전적 갱신")
async def reload_record(summoner: SummonerModel):
    return await riot_service.update_record(summoner.game_name, summoner.tag_line)
