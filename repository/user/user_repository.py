import uuid
from uuid import UUID


from database import get_db
from domain.user.user_table import User


class UserRepository:

    def __init__(self):
        self.db = next(get_db())

    def create_user(self, new_uuid: str, user_info, response):
        db_user = User(new_uuid=new_uuid)
        if user_info.get("role") == "STUDENT":
            db_user = User(
                uuid=new_uuid,
                code=user_info.get("code"),
                email=user_info.get("email"),
                nickname=user_info.get("nickname"),
                name=user_info.get("name"),
                role=user_info.get("role"),
                enrolled_at=user_info.get("enrolledAt"),
                grade=user_info.get("grade"),
                class_no=user_info.get("classNo"),
                student_no=user_info.get("studentNo")
            )
            db_user.__init__(
                new_uuid,
                user_info.get("code"),
                user_info.get("email"),
                user_info.get("nickname"),
                user_info.get("name"),
                user_info.get("role")
            )
        else:
            db_user = User(
                uuid=new_uuid,
                code=user_info.get("code"),
                email=user_info.get("email"),
                nickname=user_info.get("nickname"),
                name=user_info.get("name"),
                role=user_info.get("role")
            )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        email = self.db.query(User).filter(User.email == user_info.get("email")).first()
        return {
            "code": "200",
            "uuid": f"{email}"
        }


    def update_riot_account(self, response):
        pass


