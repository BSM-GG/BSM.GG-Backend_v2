from pydantic import BaseModel


class UserModel:
    def __init__(self, user_info):
        self.code = user_info.get("code")
        self.email = user_info.get("email")
        self.nickname = user_info.get("nickname")
        self.name = user_info.get("name")
        self.role = user_info.get("role")

        if self.role == "TEACHER": return
        self.enrolled_at = user_info.get("enrolledAt")
        self.grade = user_info.get("grade")
        self.class_no = user_info.get("classNo")
        self.student_no = user_info.get("studentNo")