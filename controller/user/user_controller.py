from fastapi import FastAPI, APIRouter

from controller.user.model.user_model import UserModel
from service.user.user_service import UserService

user_controller = APIRouter(prefix="/api/user", tags=["user"])
user_service = UserService()


@user_controller.post('', description="대충 유저 등록")
async def assign_user(auth_code: str, game_name: str, tag_line: str):
    response = await user_service.assign_user(auth_code, game_name, tag_line)
    return response


# @user_controller.post("", responses=None)
# async def get_riot_account(auth_code: str, game_name: str, tag_line: str):
#     return await user_service.assign_riot_account(game_name, tag_line)


