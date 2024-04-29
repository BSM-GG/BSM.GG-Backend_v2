from database import get_db
from domain.tables import Summoner
import time


class RiotRepository:

    def __init__(self):
        self.db = next(get_db())

    def save(self, summoner_info, rank_info, game_name: str, tag_line: str):
        db_summoner = Summoner(
            puuid=summoner_info["puuid"],
            id=summoner_info["id"],
            game_name=game_name,
            tag_line=tag_line,
            profile_icon=summoner_info["profileIconId"],
            level=summoner_info["summonerLevel"],
            tier=f"{rank_info['tier']} {rank_info['rank']}",
            lp=rank_info["leaguePoints"]
        )
        self.db.add(db_summoner)
        self.db.commit()
        self.db.refresh(db_summoner)

