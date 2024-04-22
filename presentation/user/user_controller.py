from fastapi import FastAPI, APIRouter

from service.user.user_service import UserService

user_controller = APIRouter(prefix="/user", tags=["user"])
user_service = UserService()


@user_controller.get("/", description="테스트")
async def read_user():
    return {"message": "user"}


@user_controller.get('/{auth_code}', description="OAuth login")
async def login(auth_code):
    response = await user_service.login(auth_code)
    return response
