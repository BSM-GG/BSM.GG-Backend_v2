from controller.user.model import user_model
from controller.user.model.user_model import UserModel
from database import get_db
from domain.tables import User
import time

class UserRepository:

    def __init__(self):
        self.db = next(get_db())

    def save(self, user_model: UserModel, puuid: str):
        db_user = User(
            puuid=puuid,
            code=user_model.code,
            email=user_model.email,
            nickname=user_model.nickname,
            name=user_model.name,
            role=user_model.role,
            enrolled_at=user_model.enrolled_at,
            grade=user_model.grade,
            class_no=user_model.class_no,
            student_no=user_model.student_no,
            last_updated=str(time.time()).split(".")[0]
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

    def get_user(self, email: str):
        self.db.query(User).filter(User.email == email)
