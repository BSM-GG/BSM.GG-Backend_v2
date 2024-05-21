import os
from typing import List
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from app.controller.summoner.types.match_type import MatchType, MatchResponseType
from app.controller.summoner.types.summoner_type import SummonerType, SummonerRankType
from app.controller.summoner.types.this_week_type import ThisWeekType
from app.repository.riot.riot_repository import RiotRepository
from app.service.summoner.summoner_service import SummonerService

summoner_service = SummonerService()
riot_repository = RiotRepository()
season_started = os.getenv('SEASON_STARTED_TIME')


@strawberry.type
class Query:
    @strawberry.field(description="소환사 조회")
    async def summoners(self) -> SummonerRankType:
        return await summoner_service.find_summoners()

    @strawberry.field(description="이름, 태그로 소환사 조회")
    async def summoner(self, game_name: str = "", tag_line: str = "") -> SummonerRankType:
        return await summoner_service.find_summoner_by_name(game_name, tag_line)

    @strawberry.field(description="이주의 롤창")
    async def this_week(self) -> ThisWeekType:
        return await summoner_service.find_lol_chang()

    @strawberry.field(description="전적 조회")
    async def matches(self, name: str, page: int = 0) -> MatchResponseType:
        return await summoner_service.get_matches(name, page)


schema = strawberry.Schema(query=Query, config=StrawberryConfig(auto_camel_case=False))
summoner_controller = GraphQLRouter(schema)
