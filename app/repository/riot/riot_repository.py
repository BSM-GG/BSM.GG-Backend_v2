from sqlalchemy import func, desc

from app.database import get_db
from app.domain.restapi.tables import Summoner, Match, Participant


class RiotRepository:

    def __init__(self):
        self.db = next(get_db())

    # region Summoner

    async def save(self, summoner, solo, flex, game_name: str, tag_line: str):
        db_summoner = await self.find_summoner_by_puuid(summoner["puuid"])
        if db_summoner is None:
            db_summoner = Summoner()
        db_summoner.puuid = summoner["puuid"],
        db_summoner.id = summoner["id"],
        db_summoner.game_name = game_name,
        db_summoner.tag_line = tag_line,
        db_summoner.profile_icon = summoner["profileIconId"],
        db_summoner.level = summoner["summonerLevel"],

        if len(solo) != 0:
            db_summoner.solo_tier = f"{solo[0]['tier']} {solo[0]['rank']}"
            db_summoner.solo_lp = solo[0]["leaguePoints"]
            db_summoner.solo_wins = solo[0]["wins"]
            db_summoner.solo_loses = solo[0]["losses"]
        if len(flex) != 0:
            db_summoner.flex_tier = f"{flex[0]['tier']} {flex[0]['rank']}"
            db_summoner.flex_lp = flex[0]["leaguePoints"]
            db_summoner.flex_wins = flex[0]["wins"]
            db_summoner.flex_loses = flex[0]["losses"]

        self.db.add(db_summoner)
        self.db.commit()
        self.db.refresh(db_summoner)

    async def find_summoner_by_name_and_tag(self, game_name, tag_line):
        return self.db.query(Summoner).filter(Summoner.game_name == game_name).filter(
            Summoner.tag_line == tag_line).first()

    async def find_summoner_by_puuid(self, puuid: str):
        return self.db.query(Summoner).filter(Summoner.puuid == puuid).first()

    def update_summoner_last_updated(self, puuid: str, last_match_time: int):
        if last_match_time == "":
            return
        summoner = self.db.query(Summoner).filter(Summoner.puuid == puuid).first()
        summoner.last_updated = last_match_time
        self.db.commit()

    async def find_summoner_most(self, puuid):
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

    async def find_match_by_id(self, match_id):
        return self.db.query(Match).filter(Match.match_id == match_id).first()

    # endregion

    # region Practice

    def save_participant(self, db_participant):
        self.db.add(db_participant)
        self.db.commit()
        self.db.refresh(db_participant)

    async def find_participant_by_ids(self, puuid, match_id):
        return self.db.query(Participant).filter(Participant.puuid == puuid).filter(
            Participant.match_id == match_id).first()

    # endregion
