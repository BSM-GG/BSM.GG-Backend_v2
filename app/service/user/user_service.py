import os
import uuid

from dotenv import load_dotenv

from app.controller.user.models.user_model import JwtModel
from app.repository.user.user_repository import UserRepository
from app.service.oauth.auth_service import AuthService
from app.service.riot.riot_api_service import RiotAPIService
from app.service.riot.riot_get_service import RiotGetService
from app.service.riot.riot_service import RiotService
from app.service.user.user_get_service import UserGetService
from app.utility.error.errors import InvalidAuthorizationCode, SummonerNotFound
from app.utility.jwt.jwt_util import JwtUtil

load_dotenv()


def to_model(token: str, game_name: str, tag_line: str):
    return JwtModel(
        token=token,
        game_name=game_name,
        tag_line=tag_line,
    )


class UserService:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.kr_url = os.getenv("KR_URL")
        self.asia_url = os.getenv("ASIA_URL")

        self.jwt_util = JwtUtil()
        self.user_get_service = UserGetService()
        self.auth_service = AuthService()
        self.riot_service = RiotService()
        self.riot_get_service = RiotGetService()
        self.riot_api_service = RiotAPIService()

        self.user_repository = UserRepository()

    async def assign_user(self, auth_code: str) -> JwtModel:
        auth_token = await self.auth_service.get_token(auth_code)
        if auth_token is None:
            raise InvalidAuthorizationCode(auth_code=auth_code)
        user = await self.auth_service.get_user(auth_token)

        db_user = await self.user_get_service.get_user_by_email(user['email'])
        if db_user is None:
            user_uuid = str(uuid.uuid4()).replace("-", "")
            self.user_repository.save(user_uuid, user)
            return to_model(self.jwt_util.create_token(user_uuid), "", "")

        token = self.jwt_util.create_token(db_user.uuid)
        summoner = await self.riot_get_service.get_summoner_by_puuid(db_user.puuid)
        if summoner is None:
            return to_model(token, "", "")

        riot_summoner = await self.riot_api_service.get_riot_account_by_puuid(summoner.puuid)
        if riot_summoner["gameName"] != summoner.game_name or riot_summoner["tagLine"] != summoner.tag_line:
            await self.riot_service.assign_summoner("", riot_summoner["gameName"], riot_summoner["tagLine"])
        return to_model(token, riot_summoner["gameName"], riot_summoner["tagLine"])
