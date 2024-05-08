import os
import time
from typing import List, Optional
import strawberry
from sqlalchemy import func
from strawberry.fastapi import GraphQLRouter

from app.domain.restapi.tables import Summoner, Participant, Match, User
from app.database import get_db
from app.repository.riot.riot_repository import RiotRepository

from types import SummonerType, ThisWeekType

riot_repository = RiotRepository()
season_started = os.getenv('SEASON_STARTED_TIME')



@strawberry.type
class Query:
    @strawberry.field(description="소환사 조회")
    async def summoners(self) -> List[SummonerType]:
        db = next(get_db())
        summoners = db.query(Summoner).all()
        return [SummonerType(
            puuid=summoner.puuid,
            id=summoner.id,
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
        ) for summoner in summoners]

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


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
