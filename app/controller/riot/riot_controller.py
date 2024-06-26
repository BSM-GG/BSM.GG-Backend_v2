from fastapi import APIRouter, Header

from app.controller.riot.model.riot_model import SummonerModel
from app.service.riot.riot_service import RiotService

riot_controller = APIRouter(prefix="/api/riot", tags=["riot"])
riot_service = RiotService()


@riot_controller.post("/summoner", description="소환사 등록", response_model=None)
async def assign_summoner(
        summoner: SummonerModel,
        authorization: str = Header(default=None),
) -> SummonerModel:
    summoner = await riot_service.assign_summoner(authorization, summoner.game_name, summoner.tag_line)
    return SummonerModel(game_name=summoner.game_name, tag_line=summoner.tag_line)


@riot_controller.post("/match", description="전적 갱신")
async def reload_record(summoner: SummonerModel):
    return await riot_service.update_record(summoner.game_name, summoner.tag_line)
