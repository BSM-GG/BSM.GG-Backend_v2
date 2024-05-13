from typing import List, Optional

import strawberry


@strawberry.type
class SummonerType:
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