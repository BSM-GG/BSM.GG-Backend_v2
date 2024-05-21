from typing import List

import strawberry


@strawberry.type
class ParticipantType:
    game_name: str
    tag_line: str
    solo_tier: str
    level: int
    champion: str
    champion_level: str
    spell1: str
    spell2: str
    main_perk: str
    sub_perk: int
    kill: int
    death: int
    assist: int
    damage: int
    gain_damage: int
    cs: int
    sight_ward: int
    vision_ward: int
    vision_score: int
    items: List[int]
    ward: int
    is_summoner: bool


@strawberry.type
class MatchType:
    game_type: str
    win: bool
    game_start_at: int
    game_duration: int
    participants: List[ParticipantType]


@strawberry.type
class MatchResponseType:
    matches: List[MatchType]
    page: int
