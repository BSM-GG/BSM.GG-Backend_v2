import os
from typing import List
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from app.controller.summoner.types.match_type import MatchType, MatchResponseType
from app.controller.summoner.types.summoner_type import SummonerType
from app.controller.summoner.types.this_week_type import ThisWeekType
from app.repository.riot.riot_repository import RiotRepository
from app.service.summoner.summoner_service import SummonerService

summoner_service = SummonerService()
riot_repository = RiotRepository()
season_started = os.getenv('SEASON_STARTED_TIME')


@strawberry.type
class Query:
    @strawberry.field(description="소환사 조회")
    async def summoners(self) -> List[SummonerType]:
        return await summoner_service.find_summoners()

    @strawberry.field(description="이름, 태그로 소환사 조회")
    async def summoner(self, game_name: str, tag_line: str) -> SummonerType:
        return await summoner_service.find_summoner(game_name, tag_line)

    @strawberry.field(description="이주의 롤창")
    async def this_week(self) -> ThisWeekType:
        return await summoner_service.find_lol_chang()

    @strawberry.field(description="전적 조회")
    async def matches(self, name: str, page: int) -> MatchResponseType:
        return await summoner_service.get_matches(name, page)

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
