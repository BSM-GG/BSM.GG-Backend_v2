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


@strawberry.type
class ThisWeekType:
    puuid: str
    game_name: str
    tag_line: str
    profile_icon: int
    level: int
    played_games: int
    win_games: int
    lose_games: int
    kill: int
    death: int
    assist: int
    gold_spent: int
    skill_use: int
    play_time: int
    spell_use: int
    damage: int
    gain_damage: int
    ward_place: int
    vision_score: int
    cs: int


@strawberry.type
class ParticipantType:
    game_name: str
    tag_line: str
    solo_tier: str
    level: int
    champion: str
    spell1: str
    spell2: str
    main_perk: str
    sub_perk: int
    kill: int
    death: int
    assist: int
    damage: int
    gain_damage: int
    sight_ward: int
    vision_ward: int
    vision_score: int
    items: List[int]
    ward: int


@strawberry.type
class MatchType:
    game_type: str
    win: bool
    game_start_at: int
    game_duration: int
    participants: List[ParticipantType]
