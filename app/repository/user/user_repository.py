from app.database import get_db
from app.domain.tables import User


class UserRepository:

    def __init__(self):
        self.db = next(get_db())

    def save(self, user_model, puuid: str):
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
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

    async def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    async def find_user_by_puuid(self, puuid):
        return self.db.query(User).filter(User.puuid == puuid).first()

