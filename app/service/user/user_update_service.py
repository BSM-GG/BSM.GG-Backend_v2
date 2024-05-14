from app.repository.user.user_repository import UserRepository


class UserUpdateService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def update_puuid(self, uuid: str, puuid: str):
        await self.user_repository.update_puuid_by_uuid(uuid, puuid)
