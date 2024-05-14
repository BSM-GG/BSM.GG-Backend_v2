from fastapi import APIRouter

from app.controller.user.models.user_model import UserRequestModel, JwtModel
from app.service.user.user_service import UserService

user_controller = APIRouter(prefix="/api/user", tags=["user"])
user_service = UserService()


@user_controller.post('', description="대충 유저 등록")
async def assign_user(user_model: UserRequestModel) -> JwtModel:
    response = await user_service.assign_user(user_model.auth_code)
    return JwtModel(token=response["token"], game_name=response["game_name"])


# @user_controller.post("", responses=None)
# async def get_riot_account(auth_code: str, game_name: str, tag_line: str):
#     return await user_service.assign_riot_account(game_name, tag_line)


