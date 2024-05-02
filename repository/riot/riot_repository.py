from database import get_db
from domain.tables import Summoner, Match, Participant


class RiotRepository:

    def __init__(self):
        self.db = next(get_db())

    # region Summoner

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

    async def find_summoner_by_name_and_tag(self, game_name, tag_line):
        return self.db.query(Summoner).filter(Summoner.game_name == game_name).filter(Summoner.tag_line == tag_line).first()

    async def find_summoner_by_puuid(self, puuid: str):
        return self.db.query(Summoner).filter(Summoner.puuid == puuid).first()

    def update_summoner(self, puuid: str, last_match_time: int):
        if last_match_time == "":
            return
        summoner = self.db.query(Summoner).filter(Summoner.puuid == puuid).first()
        summoner.last_updated = last_match_time
        self.db.commit()

    # endregion

    # region Match

    def save_match(self, match_id, game_start_at, game_end_at, game_duration, game_type):
        db_match = Match(
            match_id=match_id,
            game_start_at=game_start_at,
            game_end_at=game_end_at,
            game_duration=game_duration,
            game_type=game_type,
        )
        self.db.add(db_match)
        self.db.commit()
        self.db.refresh(db_match)

    def find_match_by_id(self, match_id):
        return self.db.query(Match).filter(Match.match_id == match_id).first()

    # endregion

    # region Practice

    def save_participant(self, db_participant):
        self.db.add(db_participant)
        self.db.commit()
        self.db.refresh(db_participant)

    def find_participant_by_ids(self, puuid, match_id):
        return self.db.query(Participant).filter(Participant.puuid == puuid).filter(Participant.match_id == match_id).first()

    # endregion
