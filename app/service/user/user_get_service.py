from app.repository.user.user_repository import UserRepository


class UserGetService:

    def __init__(self):
        self.user_repository = UserRepository()

    async def get_user(self, puuid):
        return await self.user_repository.find_user_by_puuid(puuid)
