from app.repository.user.user_repository import UserRepository


class UserGetService:

    def __init__(self):
        self.user_repository = UserRepository()

    async def get_user_by_email(self, email: str):
        return await self.user_repository.find_user_by_email(email)

    async def get_user_by_uuid(self, uuid: str):
        return await self.user_repository.find_user_by_uuid(uuid)

    async def get_user_by_puuid(self, puuid: str):
        return await self.user_repository.find_user_by_puuid(puuid)
