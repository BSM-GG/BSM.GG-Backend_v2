import os
from dotenv import load_dotenv

from controller.user.model.user_model import UserModel
from repository.user.user_repository import UserRepository
from service.riot.riot_service import RiotService
from service.riot.riot_api_service import RiotAPIService
from service.user.auth_service import AuthService
from service.user.user_get_service import UserGetService

load_dotenv()


class UserService:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.kr_url = os.getenv("KR_URL")
        self.asia_url = os.getenv("ASIA_URL")

        self.user_get_service = UserGetService()
        self.auth_service = AuthService()
        self.riot_service = RiotService()
        self.riot_get_service = RiotAPIService()
        self.user_repository = UserRepository()

    async def assign_user(self, auth_code: str, game_name: str, tag_line: str):
        token = await self.auth_service.get_token(auth_code)
        if token is None:
            return {
                "code": "403",
                "message": "Invalid Authorization Code"
            }
        user_info = await self.auth_service.get_user(token)
        user_model = UserModel(user_info)

        response = await self.riot_get_service.get_riot_account_by_riotAPI(game_name, tag_line)
        if response.get("status_code") == 404:
            return {
                "code": "404",
                "message": "User Not Found By Riot API"
            }

        puuid = response.get("puuid")
        if await self.user_get_service.get_user(puuid):
            return {
                "code": "409",
                "message": "Already Exists User"
            }
        self.user_repository.save(user_model, puuid)

        await self.riot_service.create_summoner(puuid, game_name, tag_line)
        await self.riot_service.update_record(game_name, tag_line)
