import os
import time
from typing import List
import strawberry
from strawberry.fastapi import GraphQLRouter
from sqlalchemy import func
from strawberry.schema.config import StrawberryConfig

from app.controller.summoner.types.summoner_type import SummonerType
from app.controller.summoner.types.this_week_type import ThisWeekType
from app.domain.restapi.tables import Summoner, Participant, Match, User
from app.database import get_db
from app.repository.riot.riot_repository import RiotRepository
from app.utility.error.errors import SummonerNotFound

riot_repository = RiotRepository()
season_started = os.getenv('SEASON_STARTED_TIME')


@strawberry.type
class Query:
    @strawberry.field(description="소환사 조회")
    async def summoners(self) -> List[SummonerType]:
        db = next(get_db())
        summoners = db.query(Summoner, User).join(User, Summoner.puuid == User.puuid).all()
        return [SummonerType(
            game_name=summoner[0].game_name,
            tag_line=summoner[0].tag_line,
            profile_icon=summoner[0].profile_icon,
            level=summoner[0].level,
            solo_tier=summoner[0].solo_tier,
            solo_lp=summoner[0].solo_lp,
            solo_wins=summoner[0].solo_wins,
            solo_loses=summoner[0].solo_loses,
            flex_tier=summoner[0].flex_tier,
            flex_lp=summoner[0].flex_lp,
            flex_wins=summoner[0].flex_wins,
            flex_loses=summoner[0].flex_loses,
            most_champions=[summoner[0].most1, summoner[0].most2, summoner[0].most3],
            email=summoner[1].email,
            code=summoner[1].code,
            nickname=summoner[1].nickname,
            name=summoner[1].name,
            role=summoner[1].role,
            is_graduate=summoner[1].is_graduate,
            enrolled_at=summoner[1].enrolled_at,
            grade=summoner[1].grade,
            class_no=summoner[1].class_no,
            student_no=summoner[1].student_no,
        ) for summoner in summoners]

    @strawberry.field(description="이름, 태그로 소환사 조회")
    async def summoner(self, game_name: str, tag_line: str) -> SummonerType:
        db = next(get_db())
        summoner = (db.query(Summoner)
                    .filter(Summoner.game_name == game_name)
                    .filter(Summoner.tag_line == tag_line)
                    .first())
        if summoner is None:
            raise SummonerNotFound(game_name=game_name, tag_line=tag_line)
        response_model = SummonerType(
            game_name=summoner.game_name,
            tag_line=summoner.tag_line,
            profile_icon=summoner.profile_icon,
            level=summoner.level,
            solo_tier=summoner.solo_tier,
            solo_lp=summoner.solo_lp,
            solo_wins=summoner.solo_wins,
            solo_loses=summoner.solo_loses,
            flex_tier=summoner.flex_tier,
            flex_lp=summoner.flex_lp,
            flex_wins=summoner.flex_wins,
            flex_loses=summoner.flex_loses,
            most_champions=[summoner.most1, summoner.most2, summoner.most3],
            email="",
            code=0,
            nickname="",
            name="",
            role="",
            is_graduate=False,
            enrolled_at=0,
            grade=0,
            class_no=0,
            student_no=0,
        )
        user = db.query(User).filter(User.puuid == summoner.puuid).first()
        if user is not None:
            response_model.email = user.email
            response_model.code = user.code
            response_model.nickname = user.nickname
            response_model.name = user.name
            response_model.role = user.role
            response_model.is_graduate = user.is_graduate
            response_model.enrolled_at = user.enrolled_at
            response_model.grade = user.grade
            response_model.class_no = user.class_no
            response_model.student_no = user.student_no
        return response_model

    @strawberry.field(description="이주의 롤창")
    async def this_week(self) -> ThisWeekType:
        db = next(get_db())
        now = int(str(time.time()).split('.')[0])
        summoner = (db.query(
            Participant.puuid.label("puuid"),
            Summoner.game_name.label("game_name"),
            Summoner.tag_line.label("tag_line"),
            Summoner.profile_icon.label("profile_icon"),
            Summoner.level.label("level"),
            func.count(Summoner.puuid).label("played_games"),
            func.sum(Participant.win).label('win_games'),
            (func.sum(Participant.puuid) - func.sum(Participant.win)).label("lose_games"),
            func.sum(Participant.kill).label("kill"),
            func.sum(Participant.death).label("death"),
            func.sum(Participant.assist).label("assist"),
            func.sum(Participant.spent_gold).label("gold_spent"),
            func.sum(Participant.skill_used).label("skill_use"),
            func.sum(Match.game_duration).label("play_time"),
            (func.sum(Participant.spell1_used) + func.sum(Participant.spell2_used)).label("spell_use"),
            func.sum(Participant.damage).label("damage"),
            func.sum(Participant.gain_damage).label("gain_damage"),
            (func.sum(Participant.sight_ward) + func.sum(Participant.vision_ward)).label("ward_place"),
            func.sum(Participant.vision_score).label("vision_score"),
            func.sum(Participant.cs).label("cs"))
                    .select_from(Participant)
                    .join(Match)
                    .join(Summoner, Participant.puuid == Summoner.puuid)
                    .join(User, Participant.puuid == User.puuid)
                    .filter(Match.game_type != "아레나")
                    .filter(Match.game_start_at >= now - 604800)
                    .group_by(Participant.puuid)
                    .order_by(func.count(Participant.puuid).desc())
                    .first())
        return ThisWeekType(
            puuid=summoner.puuid,
            game_name=summoner.game_name,
            tag_line=summoner.tag_line,
            profile_icon=summoner.profile_icon,
            level=summoner.level,
            played_games=summoner.played_games,
            win_games=summoner.win_games,
            lose_games=summoner.lose_games,
            kill=summoner.kill,
            death=summoner.death,
            assist=summoner.assist,
            gold_spent=summoner.gold_spent,
            skill_use=summoner.skill_use,
            play_time=summoner.play_time,
            spell_use=summoner.spell_use,
            damage=summoner.damage,
            gain_damage=summoner.gain_damage,
            ward_place=summoner.ward_place,
            vision_score=summoner.vision_score,
            cs=summoner.cs,
        )

    # @strawberry.filed(description="소환사 전적 검색")
    # async def summoner_analyze(self, game_name: str, tag_line: str, page: int = 0) -> MatchType:
    #     db = next(get_db())
    #     offset = (page-1) * 10
    #     limit = 10
    #
    #     match_ids = db.query(Match.match_id).offset(offset).limit(limit).all()
    # for match_id in match_ids:
    #     participants = (db.query(Participant.puuid)
    #                     .select_from(Participant)
    #                     .join(Match)
    #                     .filter(Match.match_id == match_id)
    #                     .all())
    #     part_list = [ParticipantType(
    #         game_name=participant.game_name
    #         tag_line=participant.
    #         solo_tier=participant.
    #         level=participant.
    #         champion=participant.
    #         spell1=participant.
    #         spell2=participant.
    #         main_perk=participant.
    #         sub_perk=participant.
    #         kill=participant.
    #         death=participant.
    #         assist=participant.
    #         damage=participant.
    #         gain_damage=participant.
    #         sight_ward=participant.
    #         vision_ward=participant.
    #         vision_score=participant.
    #         items: List[int]
    #         ward
    #     ) for participant in participants]


schema = strawberry.Schema(query=Query, config=StrawberryConfig(auto_camel_case=False))
summoner_controller = GraphQLRouter(schema)
