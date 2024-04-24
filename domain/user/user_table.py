from uuid import UUID

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from database import Base
from database import ENGINE


class UserTable(Base):
    __tablename__ = 'user'
    # user info
    uuid = Column(String, primary_key=True)
    code = Column(Integer, nullable=False)
    nick_name = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    enrolledAt = Column(Integer)
    grade = Column(Integer)
    classNo = Column(Integer)
    studentNo = Column(Integer)
    role = Column(String)
    profile_url = Column(String)
    # riot info
    puuid = Column(String)
    game_name = Column(String)
    tag_line = Column(String)
    # util
    last_updated = Column(String)
