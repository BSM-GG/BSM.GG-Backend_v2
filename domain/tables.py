from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'user'

    # riot puuid
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


class Summoner(Base):
    __tablename__ = 'summoner'
    # riot puuid
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

    # util
    last_updated = Column(String(30), default=1713582000)


class Match(Base):
    __tablename__ = 'match'
    # match id
    match_id = Column(String(100), primary_key=True)

    # match info
    game_start_at = Column(Integer)
    game_end_at = Column(Integer)
    game_duration = Column(Integer)
    game_type = Column(String(10))

    # relationship
    participant = relationship("Participant", back_populates="match")


class Participant(Base):
    __tablename__ = 'participant'
    # riot puuid
    puuid = Column(String(100), primary_key=True)

    # match id
    match_id = Column(String(100), ForeignKey("match.match_id"), primary_key=True)

    # info
    win = Column(Boolean)
    champion = Column(String(100))
    champion_level = Column(Integer)
    lane = Column(String(20))
    kill = Column(Integer)
    assist = Column(Integer)
    death = Column(Integer)
    cs = Column(Integer)
    damage = Column(Integer)
    damage_rate = Column(Integer)
    gain_damage = Column(Integer)
    heal = Column(Integer)
    vision_ward = Column(Integer)
    sight_ward = Column(Integer)
    vision_score = Column(Integer)
    spell1 = Column(String(50))
    spell2 = Column(String(50))
    item1 = Column(Integer)
    item2 = Column(Integer)
    item3 = Column(Integer)
    item4 = Column(Integer)
    item5 = Column(Integer)
    item6 = Column(Integer)
    ward = Column(Integer)
    main_perk = Column(String(50))
    main_perk_part1 = Column(String(50))
    main_perk_part2 = Column(String(50))
    main_perk_part3 = Column(String(50))
    sub_perk_part1 = Column(String(50))
    sub_perk_part2 = Column(String(50))
    offense_perk = Column(Integer)
    flex_perk = Column(Integer)
    defense_perk = Column(Integer)

    # relationship
    match = relationship("Match", back_populates="participant")
