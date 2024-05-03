from fastapi import APIRouter

from app.controller.riot.model.riot_model import MatchesCreate
from app.service.riot.riot_service import RiotService

riot_controller = APIRouter(prefix="/api/riot", tags=["riot"])
riot_service = RiotService()


# @riot_controller.post('', description="대충 유저 등록")
# async def assign_riot(email: str, game_name, tag_line):
#     return await riot_service.create_summoner(email, game_name, tag_line)

@riot_controller.post("", description="유저 매치 정보 업데이트")
async def reload_record(user: MatchesCreate):
    return await riot_service.update_record(user.game_name, user.tag_line)
