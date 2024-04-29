from fastapi import FastAPI, APIRouter

from controller.user.model.user_model import UserModel, UserCreate
from service.riot.riot_service import RiotService
from service.user.user_service import UserService

riot_controller = APIRouter(prefix="/api/riot", tags=["riot"])
riot_service = RiotService()


@riot_controller.post('', description="대충 유저 등록")
async def assign_riot(email: str):
    return await riot_service.create_summoner()
