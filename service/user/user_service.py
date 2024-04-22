import httpx
import asyncio

from service.user.auth_service import AuthService


class UserService:

    def __init__(self):
        self.auth_service = AuthService()

    async def login(self, auth_code):
        async with httpx.AsyncClient() as client:
            token = await self.auth_service.get_token(client, auth_code)
            print(token)
            user_info = await self.auth_service.get_user(client, token)
            print(user_info)
            return user_info


