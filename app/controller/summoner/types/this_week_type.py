from typing import List, Optional

import strawberry


@strawberry.type
class ThisWeekType:
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

    email: str
    code: int
    nickname: str
    name: str
    role: str
    is_graduate: bool
    enrolled_at: int
    grade: int
    class_no: int
    student_no: int

    ranking: int

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

