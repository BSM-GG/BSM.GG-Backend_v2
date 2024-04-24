from fastapi import FastAPI, APIRouter

from controller.user.base_models.base_models import UserRiotAccount
from service.user.user_service import UserService

user_controller = APIRouter(prefix="/api/user", tags=["user"])
user_service = UserService()


@user_controller.get('/{auth_code}', description="OAuth login")
async def assign_user(auth_code):
    response = await user_service.assign_user(auth_code)
    return response


@user_controller.get("", response_model=UserRiotAccount)
async def get_riot_account(game_name: str, tag_line: str):
    return await user_service.assign_riot_account(game_name, tag_line)


