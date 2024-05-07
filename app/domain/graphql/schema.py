from typing import List, Optional
import strawberry
from strawberry.fastapi import GraphQLRouter

from app.domain.restapi.tables import Summoner
from app.database import get_db
from app.repository.riot.riot_repository import RiotRepository

riot_repository = RiotRepository()


@strawberry.type
class SummonerType:
    puuid: str
    id: str
    game_name: str
    tag_line: str
    profile_icon: int
    level: int
    solo_tier: str
    solo_lp: int
    solo_wins: int
    solo_loses: int
    flex_tier: str
    flex_lp: int
    flex_wins: int
    flex_loses: int
    most_champions: List[Optional[str]]


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


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
