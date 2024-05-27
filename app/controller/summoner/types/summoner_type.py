from typing import List, Optional, Annotated, Union

import strawberry


@strawberry.type
class SummonerType:
    # summoner info
    game_name: str = ""
    tag_line: str = ""
    profile_icon: int = 0
    level: int = 0
    solo_tier: str = ""
    solo_lp: int = 0
    solo_wins: int = 0
    solo_loses: int = 0
    flex_tier: str = ""
    flex_lp: int = 0
    flex_wins: int = 0
    flex_loses: int = 0
    most_champions: List[Optional[str]]

    # user info
    email: str = ""
    code: int = 0
    nickname: str = ""
    name: str = ""
    role: str = ""
    is_graduate: bool = False
    enrolled_at: int = 0
    grade: int = 0
    class_no: int = 0
    student_no: int = 0

    solo_point: int = 0
    ranking: int = 0


@strawberry.type
class SummonerRankType:
    summoner_types: List[SummonerType]
    user_count: int
