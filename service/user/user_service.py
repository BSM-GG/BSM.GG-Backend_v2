import os
from dotenv import load_dotenv

from controller.user.model.user_model import UserModel
from repository.user.user_repository import UserRepository
from service.riot.riot_service import RiotService
from service.user.auth_service import AuthService

load_dotenv()


class UserService:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.kr_url = os.getenv("KR_URL")
        self.asia_url = os.getenv("ASIA_URL")

        self.auth_service = AuthService()
        self.user_repository = UserRepository()
        self.riot_service = RiotService()

    async def assign_user(self, auth_code: str, game_name: str, tag_line: str):
        token = await self.auth_service.get_token(auth_code)
        if token is None:
            return {
                "code": "403",
                "message": "Invalid Authorization Code"
            }
        user_info = await self.auth_service.get_user(token)
        user_model = UserModel(user_info)

        response = await self.riot_service.get_riot_account(game_name, tag_line)
        if response.get("status_code") == 404:
            return {
                "code": "404",
                "message": "User Not Found By Riot API"
            }

        puuid = response.get("puuid")
        self.user_repository.save(user_model, puuid)

        await self.riot_service.create_summoner(puuid, game_name, tag_line)
