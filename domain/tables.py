from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'user'

    # uuid
    puuid = Column(String(100), primary_key=True)

    # common info
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


class Summoner(Base):
    __tablename__ = 'summoner'
    # uuid
    puuid = Column(String(100), primary_key=True)

    # riot info
    id = Column(String(100))
    game_name = Column(String(20))
    tag_line = Column(String(20))
    profile_icon = Column(Integer)
    level = Column(Integer)
    tier = Column(String(50))
    lp = Column(Integer)
    most1 = Column(String(50))
    most2 = Column(String(50))
    most3 = Column(String(50))
    # win_rate = Column(Integer)
    # win_games = Column(Integer)
    # lose_game = Column(Integer)
    # kill = Column(Integer)
    # death = Column(Integer)
    # assist = Column(Integer)
    # play_time = Column(Integer)


class Match(Base):
    __tablename__ = 'match'
    # match id
    match_id = Column(String(100), primary_key=True)

    # match info
    result = Column(Boolean)
    played_champ = Column(String(50))
    played_time = Column(Integer)
    kill = Column(Integer)
    death = Column(Integer)
    assist = Column(Integer)
    play_time = Column(Integer)
    end_at = Column(String(30))


