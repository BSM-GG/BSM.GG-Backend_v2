import strawberry


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