import os
import uuid

import requests
from dotenv import load_dotenv

from repository.user.user_repository import UserRepository
from service.user.auth_service import AuthService

load_dotenv()


class UserService:

    def __init__(self):
        self.api_key = os.environ["API_KEY"]
        self.kr_url = os.getenv("KR_URL")
        self.asia_url = os.getenv("ASIA_URL")

        self.auth_service = AuthService()
        self.user_repository = UserRepository()

    async def assign_user(self, auth_code: str, game_name: str, tag_line: str):
        token = await self.auth_service.get_token(auth_code)
        if token is None:
            return {
                "code": "403",
                "message": "Invalid Authorization Code"
            }

        user_info = await self.auth_service.get_user(token)

        response = requests.get(f"{self.asia_url}/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={self.api_key}")
        if response.json().get("status_code") != "200":
            return {
                "code": "404",
                "message": "User Not Found"
            }

        new_uuid = str(uuid.uuid4()).replace("-", "")
        return self.user_repository.create_user(new_uuid, user_info, response.json().text())
