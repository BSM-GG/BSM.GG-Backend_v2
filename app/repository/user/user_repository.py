from app.database import get_db
from app.domain.restapi.tables import User


class UserRepository:

    def __init__(self):
        self.db = next(get_db())

    def save(self, uuid: str, user):
        db_user = User(
            uuid=uuid,
            email=user["email"],
            code=user["code"],
            nickname=user["nickname"],
            name=user["name"],
            role=user["role"],
            is_graduate=user["isGraduate"],
            enrolled_at=user["enrolledAt"],
            grade=user["grade"],
            class_no=user["classNo"],
            student_no=user["studentNo"],
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

    def find_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def find_user_by_uuid(self, uuid: str):
        return self.db.query(User).filter(User.uuid == uuid).first()

    def update_puuid_by_uuid(self, uuid: str, puuid: str):
        user = self.find_user_by_uuid(uuid)
        user.puuid = puuid
        self.db.commit()


