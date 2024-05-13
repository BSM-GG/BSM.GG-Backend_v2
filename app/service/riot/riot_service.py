import json
import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

from app.domain.restapi.tables import Participant
from app.repository.riot.riot_repository import RiotRepository
from app.repository.user.user_repository import UserRepository
from app.service.riot.mapping.name_mapping import QUEUE_TYPE, PERKS, SPELL_NAME
from app.service.riot.riot_api_service import RiotAPIService
from app.service.riot.riot_get_service import RiotGetService
from app.utility.error.errors import InvalidToken, UserNotFoundByRiotAPI
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
        self.riot_repository = RiotRepository()
        self.user_repository = UserRepository()

    async def assign_summoner(self, token: str, game_name: str, tag_line: str):
        user = self.jwt_util.decode_token(token)
        if user in None:
            raise InvalidToken(token=token)

        response = await self.riot_api_service.get_riot_account_by_riotAPI(game_name, tag_line)
        if response.json().get("status_code") == 404:
            raise UserNotFoundByRiotAPI(game_name=game_name, tag_line=tag_line)
        summoner = json.loads(response.text)

        rank = await self.riot_api_service.get_rank_info_by_riotAPI(summoner["id"])

        solo = list(filter(lambda item: item['queueType'] == 'RANKED_SOLO_5x5', rank))
        flex = list(filter(lambda item: item['queueType'] == 'RANKED_FLEX_SR', rank))

        self.riot_repository.save(summoner, solo, flex, game_name, tag_line)

    async def send_match_query(self, match_id: str) -> int:
        if await self.riot_get_service.find_match(match_id):
            return 0
        match = await self.riot_api_service.get_match_data_by_riotAPI(match_id)

        # match info
        game_start_at = int(str(match["info"]["gameCreation"])[:-3])
        game_end_at = int(str(match["info"]["gameEndTimestamp"])[:-3])
        game_duration = match["info"]["gameDuration"]
        game_type = QUEUE_TYPE[match["info"]["queueId"]]
        self.riot_repository.save_match(match_id, game_start_at, game_end_at, game_duration, game_type)

        participants = match["info"]["participants"]
        for participant in participants:
            puuid = participant["puuid"]
            if await self.riot_get_service.find_participant(puuid, match_id):
                continue

            main_perks = participant["perks"]["styles"][0]["selections"]
            sub_perks = participant["perks"]["styles"][1]["selections"]
            db_participant = Participant(
                puuid=puuid,
                match_id=match_id,
                game_name=participant["riotIdGameName"],
                tag_line=participant["riotIdTagline"],
                win=participant["win"],
                champion=participant["championName"],
                champion_level=participant["champLevel"],
                lane=participant["lane"],
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
                main_perk_part1=next((perk for perk in PERKS if perk["id"] == main_perks[1]["perk"]), {"name": ""})["name"],
                main_perk_part2=next((perk for perk in PERKS if perk["id"] == main_perks[2]["perk"]), {"name": ""})["name"],
                main_perk_part3=next((perk for perk in PERKS if perk["id"] == main_perks[3]["perk"]), {"name": ""})["name"],
                sub_style=participant["perks"]["styles"][1]["style"],
                sub_perk_part1=next((perk for perk in PERKS if perk["id"] == sub_perks[0]["perk"]), {"name": ""})["name"],
                sub_perk_part2=next((perk for perk in PERKS if perk["id"] == sub_perks[1]["perk"]), {"name": ""})["name"],
                offense_perk=participant["perks"]["statPerks"]["offense"],
                flex_perk=participant["perks"]["statPerks"]["flex"],
                defense_perk=participant["perks"]["statPerks"]["defense"],
            )
            self.riot_repository.save_participant(db_participant)

        return match.game_end_at

    async def update_record(self, game_name: str, tag_line: str):

        summoner = await self.riot_get_service.find_summoner_by_game_name_and_tag_line(game_name, tag_line)
        if not summoner:
            return {
                "code": "404",
                "message": "Cannot Find Summoner"
            }

        match_ids = await self.riot_api_service.get_matches_by_riotAPI(summoner.puuid, summoner.last_updated)
        while True:
            if len(match_ids) == 0:
                break

            last_match_time = 0
            with ThreadPoolExecutor(max_workers=16) as executor:
                last_match_times = list(executor.map(self.send_match_query, match_ids))

            if last_match_time != 0:
                self.riot_repository.update_summoner_last_updated(summoner.puuid, last_match_time)

            if len(match_ids) < 100:
                break

        mosts = self.riot_repository.find_summoner_most(summoner.puuid)
        self.riot_repository.update_summoner_mosts(summoner.puuid, mosts)
