from app.repository.user.user_repository import UserRepository


class UserGetService:

    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_by_email(self, email: str):
        return self.user_repository.find_user_by_email(email)

    def get_user_by_uuid(self, uuid: str):
        return self.user_repository.find_user_by_uuid(uuid)
