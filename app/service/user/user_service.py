import os
import uuid

from dotenv import load_dotenv

from app.repository.user.user_repository import UserRepository
from app.service.oauth.auth_service import AuthService
from app.service.riot.riot_get_service import RiotGetService
from app.service.riot.riot_service import RiotService
from app.service.user.user_get_service import UserGetService
from app.utility.error.errors import InvalidAuthorizationCode, SummonerNotFound
from app.utility.jwt.jwt_util import JwtUtil

load_dotenv()


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

        self.user_repository = UserRepository()

    async def assign_user(self, auth_code: str) -> dict:
        auth_token = await self.auth_service.get_token(auth_code)
        if auth_token is None:
            raise InvalidAuthorizationCode(auth_code=auth_code)
        user = await self.auth_service.get_user(auth_token)

        db_user = await self.user_get_service.get_user_by_email(user['email'])
        if db_user is None:
            user_uuid = str(uuid.uuid4()).replace("-", "")
            self.user_repository.save(user_uuid, user)
            return {
                "token": self.jwt_util.create_token(user_uuid),
                "game_name": "",
                "tag_line": "",
            }

        summoner = await self.riot_get_service.get_summoner_by_puuid(db_user.puuid)
        if summoner is None:
            return {
                "token": self.jwt_util.create_token(db_user.uuid),
                "game_name": "",
                "tag_line": "",
            }

        return {
            "token": self.jwt_util.create_token(db_user.uuid),
            "game_name": summoner.game_name,
            "tag_line": summoner.tag_line,
        }

        # await self.riot_service.update_record(game_name, tag_line)
