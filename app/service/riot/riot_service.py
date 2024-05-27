import os

from dotenv import load_dotenv

from app.domain.restapi.tables import Participant
from app.repository.riot.riot_repository import RiotRepository
from app.repository.user.user_repository import UserRepository
from app.utility.mapping.name_mapping import QUEUE_TYPE, PERKS, SPELL_NAME, TEAM
from app.service.riot.riot_api_service import RiotAPIService
from app.service.riot.riot_get_service import RiotGetService
from app.service.user.user_update_service import UserUpdateService
from app.utility.error.errors import InvalidToken, SummonerNotFoundByRiotAPI, RiotAPIForbidden, SummonerNotFound
from app.utility.jwt.jwt_util import JwtUtil

load_dotenv()


class RiotService:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.kr_url = os.getenv("KR_URL")
        self.asia_url = os.getenv("ASIA_URL")
        self.season_started_time = os.getenv("SEASON_STARTED_TIME")

        self.jwt_util = JwtUtil()
        self.riot_api_service = RiotAPIService()
        self.riot_get_service = RiotGetService()
        self.user_get_service = UserRepository()
        self.user_update_service = UserUpdateService()
        self.riot_repository = RiotRepository()
        self.user_repository = UserRepository()

    async def assign_summoner(self, authorization: str, game_name: str, tag_line: str):
        response = await self.riot_api_service.get_riot_account_by_riotAPI(game_name, tag_line)
        if 'status' in response:
            if response['status']['status_code'] == 403:
                raise RiotAPIForbidden()
            if response['status']['status_code'] == 404:
                raise SummonerNotFoundByRiotAPI(game_name=game_name, tag_line=tag_line)
        summoner_id = await self.save_summoner(response["puuid"], game_name, tag_line)
        rank = await self.riot_api_service.get_rank_info_by_riotAPI(summoner_id)
        solo = list(filter(lambda item: item['queueType'] == 'RANKED_SOLO_5x5', rank))
        flex = list(filter(lambda item: item['queueType'] == 'RANKED_FLEX_SR', rank))
        summoner = await self.riot_repository.update_summoner_rank(response["puuid"], solo, flex)

        if authorization == "": return
        user = await self.jwt_util.decode_token(authorization)
        if user is None:
            raise InvalidToken(token=authorization)
        await self.user_update_service.update_puuid(user.uuid, response["puuid"])
        return summoner

    async def save_summoner(self, puuid: str, game_name: str, tag_line: str):
        summoner = await self.riot_api_service.get_summoner_info_by_riotAPI(puuid)
        await self.riot_repository.save(summoner, game_name, tag_line)
        return summoner["id"]

    async def update_record(self, game_name: str, tag_line: str):
        summoner = await self.riot_get_service.get_summoner_by_game_name_and_tag_line(game_name, tag_line)
        if not summoner:
            raise SummonerNotFound(game_name=game_name, tag_line=tag_line)

        match_ids = await self.riot_api_service.get_matches_by_riotAPI(summoner.puuid, summoner.last_updated)
        while True:
            if len(match_ids) == 0:
                break

            last_match_time = 0
            for match_id in match_ids:
                if await self.riot_get_service.get_match(match_id):
                    continue
                match = await self.riot_api_service.get_match_data_by_riotAPI(match_id)
                await self.save_match(match)

                participants = match["info"]["participants"]
                summoners = await self.save_participants(match_id, participants)
                last_match_time = int(str(match["info"]["gameEndTimestamp"])[:-3])

                for s in summoners:
                    await self.save_summoner(
                        s["puuid"],
                        s["game_name"],
                        s["tag_line"],
                    )

            if last_match_time != 0:
                self.riot_repository.update_summoner_last_updated(summoner.puuid, last_match_time)

            if len(match_ids) < 100:
                break

        await self.assign_summoner("", game_name, tag_line)
        mosts = await self.riot_repository.find_summoner_most(summoner.puuid)
        self.riot_repository.update_summoner_mosts(summoner.puuid, mosts)

    async def save_participants(self, match_id, participants: list) -> list[dict]:
        summoners = []
        cnt = 0
        for participant in participants:
            puuid = participant["puuid"]
            main_perks = participant["perks"]["styles"][0]["selections"]
            sub_perks = participant["perks"]["styles"][1]["selections"]
            db_participant = Participant(
                puuid=puuid,
                match_id=match_id,
                win=participant["win"],
                champion=participant["championName"],
                champion_level=participant["champLevel"],
                kill=participant["kills"],
                assist=participant["assists"],
                death=participant["deaths"],
                cs=participant["totalMinionsKilled"],
                damage=participant["totalDamageDealt"],
                damage_rate=round(participant["challenges"]["teamDamagePercentage"] * 100),
                gain_damage=participant["totalDamageTaken"],
                heal=participant["totalHeal"],
                earned_gold=participant["goldEarned"],
                spent_gold=participant["goldSpent"],
                vision_ward=participant["visionWardsBoughtInGame"],
                sight_ward=participant["sightWardsBoughtInGame"],
                vision_score=participant["visionScore"],
                skill_used=participant["challenges"]["abilityUses"],
                spell1=SPELL_NAME[participant["summoner1Id"]],
                spell2=SPELL_NAME[participant["summoner2Id"]],
                spell1_used=participant["summoner1Casts"],
                spell2_used=participant["summoner2Casts"],
                item1=participant["item0"],
                item2=participant["item1"],
                item3=participant["item2"],
                item4=participant["item3"],
                item5=participant["item4"],
                item6=participant["item5"],
                ward=participant["item6"],
                main_perk=next((perk for perk in PERKS if perk["id"] == main_perks[0]["perk"]), {"name": ""})["name"],
                main_perk_part1=next((perk for perk in PERKS if perk["id"] == main_perks[1]["perk"]), {"name": ""})[
                    "name"],
                main_perk_part2=next((perk for perk in PERKS if perk["id"] == main_perks[2]["perk"]), {"name": ""})[
                    "name"],
                main_perk_part3=next((perk for perk in PERKS if perk["id"] == main_perks[3]["perk"]), {"name": ""})[
                    "name"],
                sub_style=participant["perks"]["styles"][1]["style"],
                sub_perk_part1=next((perk for perk in PERKS if perk["id"] == sub_perks[0]["perk"]), {"name": ""})[
                    "name"],
                sub_perk_part2=next((perk for perk in PERKS if perk["id"] == sub_perks[1]["perk"]), {"name": ""})[
                    "name"],
                offense_perk=participant["perks"]["statPerks"]["offense"],
                flex_perk=participant["perks"]["statPerks"]["flex"],
                defense_perk=participant["perks"]["statPerks"]["defense"],
            )
            if participant["lane"] != "NONE":
                db_participant.lane = (cnt % 5)+1
                db_participant.team = TEAM[cnt//5]
            self.riot_repository.save_participant(db_participant)

            cnt += 1
            summoners.append({
                "puuid": puuid,
                "game_name": participant["riotIdGameName"],
                "tag_line": participant["riotIdTagline"],
            })

        return summoners

    async def save_match(self, match):
        match_id = match["metadata"]["matchId"]
        game_start_at = int(str(match["info"]["gameCreation"])[:-3])
        game_end_at = int(str(match["info"]["gameEndTimestamp"])[:-3])
        game_duration = match["info"]["gameDuration"]
        game_type = QUEUE_TYPE[match["info"]["queueId"]]
        self.riot_repository.save_match(match_id, game_start_at, game_end_at, game_duration, game_type)
