from uuid import UUID

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from database import Base
from database import engine


class User(Base):
    __tablename__ = 'user'
    # common info
    uuid = Column(String(32), primary_key=True)
    code = Column(Integer, nullable=False)
    email = Column(String(32), nullable=False, unique=True)
    nickname = Column(String(32), nullable=False)
    name = Column(String(32), nullable=False)
    role = Column(String(20), nullable=False)

    # student info
    enrolled_at = Column(Integer)
    grade = Column(Integer)
    class_no = Column(Integer)
    student_no = Column(Integer)

    # util
    last_updated = Column(String(30))

    # def __init__(self, uuid, code, email, nickname, name, role):
    #     this.uuid = uuid

class Summoner(Base):
    __tablename__ = 'summoner'


    # riot info
    puuid = Column(String(100))
    game_name = Column(String(20))
    tag_line = Column(String(20))