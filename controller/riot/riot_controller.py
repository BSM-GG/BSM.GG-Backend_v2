from fastapi import APIRouter

from service.riot.riot_service import RiotService

riot_controller = APIRouter(prefix="/api/riot", tags=["riot"])
riot_service = RiotService()


# @riot_controller.post('', description="대충 유저 등록")
# async def assign_riot(email: str, game_name, tag_line):
#     return await riot_service.create_summoner(email, game_name, tag_line)
