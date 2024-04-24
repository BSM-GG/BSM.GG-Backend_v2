import os
import requests
from dotenv import load_dotenv

from service.user.auth_service import AuthService

load_dotenv()


class UserService:

    def __init__(self):
        self.auth_service = AuthService()
        self.api_key = os.environ["API_KEY"]
        self.kr_url = os.getenv("KR_URL")
        self.asia_url = os.getenv("ASIA_URL")

    async def assign_user(self, auth_code):
        token = await self.auth_service.get_token(auth_code)
        user_info = await self.auth_service.get_user(token)
        return user_info

    async def assign_riot_account(self, game_name: str, tag_line: str):
        response = requests.get(
            f"{self.asia_url}/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={self.api_key}"
        )
        return response.json()

