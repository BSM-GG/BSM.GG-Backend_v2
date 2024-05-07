from sqlalchemy import func, desc

from app.database import get_db
from app.domain.restapi.tables import Summoner, Match, Participant


class RiotRepository:

    def __init__(self):
        self.db = next(get_db())

    # region Summoner

    def save(self, summoner_info, solo_info, flex_info, game_name: str, tag_line: str):
        solo_tier = ""
        solo_lp = 0
        solo_wins = 0
        solo_loses = 0

        flex_tier = ""
        flex_lp = 0
        flex_wins = 0
        flex_loses = 0

        if len(solo_info) != 0:
            solo_tier = f"{solo_info[0]['tier']} {solo_info[0]['rank']}"
            solo_lp = solo_info[0]["leaguePoints"]
            solo_wins = solo_info[0]["wins"]
            solo_loses = solo_info[0]["losses"]
        if len(flex_info) != 0:
            flex_tier = f"{flex_info[0]['tier']} {flex_info[0]['rank']}"
            flex_lp = flex_info[0]["leaguePoints"]
            flex_wins = flex_info[0]["wins"]
            flex_loses = flex_info[0]["losses"]
        db_summoner = Summoner(
            puuid=summoner_info["puuid"],
            id=summoner_info["id"],
            game_name=game_name,
            tag_line=tag_line,
            profile_icon=summoner_info["profileIconId"],
            level=summoner_info["summonerLevel"],
            solo_tier=solo_tier,
            solo_lp=solo_lp,
            solo_wins=solo_wins,
            solo_loses=solo_loses,
            flex_tier=flex_tier,
            flex_lp=flex_lp,
            flex_wins=flex_wins,
            flex_loses=flex_loses,
        )
        self.db.add(db_summoner)
        self.db.commit()
        self.db.refresh(db_summoner)

    async def find_summoner_by_name_and_tag(self, game_name, tag_line):
        return self.db.query(Summoner).filter(Summoner.game_name == game_name).filter(
            Summoner.tag_line == tag_line).first()

    async def find_summoner_by_puuid(self, puuid: str):
        return self.db.query(Summoner).filter(Summoner.puuid == puuid).first()

    def update_summoner(self, puuid: str, last_match_time: int):
        if last_match_time == "":
            return
        summoner = self.db.query(Summoner).filter(Summoner.puuid == puuid).first()
        summoner.last_updated = last_match_time
        self.db.commit()

    def find_summoner_most(self, puuid):
        return (self.db.query(Participant.champion, func.count(Participant.champion))
                .join(Match)
                .filter(Participant.puuid == puuid)
                .filter(Match.game_type == "솔랭")
                .filter(Match.game_start_at >= 1704855600)
                .group_by(Participant.champion)
                .order_by(desc(func.count(Participant.champion)))
                .limit(3)
                .all())

    def update_summoner_mosts(self, puuid, mosts):
        summoner = self.db.query(Summoner).filter(Summoner.puuid == puuid).first()
        length = len(mosts)
        if length == 0:
            return
        if length >= 1:
            summoner.most1 = mosts[0][0]
        if length >= 2:
            summoner.most2 = mosts[1][0]
        if length == 3:
            summoner.most3 = mosts[2][0]
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
        return self.db.query(Participant).filter(Participant.puuid == puuid).filter(
            Participant.match_id == match_id).first()

    # endregion
