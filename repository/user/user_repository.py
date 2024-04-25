import uuid
from uuid import UUID

from controller.user.model.user_model import UserModel
from database import get_db
from domain.user.user_table import User


class UserRepository:

    def __init__(self):
        self.db = next(get_db())

    def create_user(self, new_uuid: str, user_model: UserModel, response):
        db_user = User(
            uuid=new_uuid,
            code=user_model.code,
            email=user_model.email,
            nickname=user_model.nickname,
            name=user_model.name,
            role=user_model.role,
            enrolled_at=user_model.enrolled_at,
            grade=user_model.grade,
            class_no=user_model.class_no,
            student_no=user_model.student_no,
            puuid=response.get("puuid"),
            game_name=response.get("gameName"),
            tag_line=response.get("tagLine")
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return {
            "code": "200",
            "uuid": f"success"
        }

    def update_riot_account(self, response):
        pass
