import os
from dotenv import load_dotenv

from domain.tables import Participant
from repository.riot.riot_repository import RiotRepository
from repository.user.user_repository import UserRepository
from service.riot.mapping.name_mapping import QUEUE_TYPE, PERKS, SPELL_NAME
from service.riot.riot_api_service import RiotAPIService

load_dotenv()


class RiotService:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.kr_url = os.getenv("KR_URL")
        self.asia_url = os.getenv("ASIA_URL")
        self.season_started_time = os.getenv("SEASON_STARTED_TIME")

        self.riot_api_service = RiotAPIService()
        self.user_get_service = UserRepository()
        self.riot_repository = RiotRepository()
        self.user_repository = UserRepository()

    async def create_summoner(self, puuid: str, game_name: str, tag_line: str):
        summoner_info = await self.riot_api_service.get_summoner_info_by_riotAPI(puuid)
        rank_info = await self.riot_api_service.get_rank_info_by_riotAPI(summoner_info["id"])

        rank_info = rank_info[["queueType"] == "RANKED_SOLO_5x5"]
        self.riot_repository.save(summoner_info, rank_info, game_name, tag_line)

    async def update_record(self, game_name: str, tag_line: str):

        summoner = await self.riot_api_service.find_summoner(game_name, tag_line)
        if not summoner:
            return {
                "code": "404",
                "message": "Cannot Find Summoner"
            }

        matches = await self.riot_api_service.get_matches_by_riotAPI(summoner.puuid, summoner.last_updated)
        while True:
            if len(matches) == 0:
                return

            last_match_time = ""
            for match_id in matches:
                if await self.riot_api_service.find_match(match_id):
                    continue
                match = await self.riot_api_service.get_match_data_by_riotAPI(match_id)

                # match info
                game_start_at = int(str(match["info"]["gameCreation"])[:-4])
                game_end_at = int(str(match["info"]["gameEndTimestamp"])[:-4])
                game_duration = match["info"]["gameDuration"]
                game_type = QUEUE_TYPE[match["info"]["queueId"]]
                self.riot_repository.save_match(match_id, game_start_at, game_end_at, game_duration, game_type)

                participants = match["info"]["participants"]
                for participant in participants:
                    puuid = participant["puuid"]
                    if await self.riot_api_service.find_participant(puuid, match_id):
                        continue
                    main_perks = participant["perks"]["styles"][0]["selections"]
                    sub_perks = participant["perks"]["styles"][1]["selections"]
                    db_participant = Participant(
                        puuid=puuid,
                        match_id=match_id,
                        win=participant["win"],
                        champion=participant["championName"],
                        champion_level=participant["champLevel"],
                        lane=participant["lane"],
                        kill=participant["kills"],
                        assist=participant["assists"],
                        death=participant["deaths"],
                        cs=participant["totalMinionsKilled"],
                        damage=participant["totalDamageDealt"],
                        damage_rate=round(participant["challenges"]["teamDamagePercentage"]*100),
                        gain_damage=participant["totalDamageTaken"],
                        heal=participant["totalHeal"],
                        vision_ward=participant["visionWardsBoughtInGame"],
                        sight_ward=participant["sightWardsBoughtInGame"],
                        vision_score=participant["visionScore"],
                        spell1=SPELL_NAME[participant["summoner1Id"]],
                        spell2=SPELL_NAME[participant["summoner2Id"]],
                        item1=participant["item0"],
                        item2=participant["item1"],
                        item3=participant["item2"],
                        item4=participant["item3"],
                        item5=participant["item4"],
                        item6=participant["item5"],
                        ward=participant["item6"],
                        main_perk=next((perk for perk in PERKS if perk["id"] == main_perks[0]["perk"]), False)["name"],
                        main_perk_part1=next((perk for perk in PERKS if perk["id"] == main_perks[1]["perk"]), False)["name"],
                        main_perk_part2=next((perk for perk in PERKS if perk["id"] == main_perks[2]["perk"]), False)["name"],
                        main_perk_part3=next((perk for perk in PERKS if perk["id"] == main_perks[3]["perk"]), False)["name"],
                        sub_perk_part1=next((perk for perk in PERKS if perk["id"] == sub_perks[0]["perk"]), False)["name"],
                        sub_perk_part2=next((perk for perk in PERKS if perk["id"] == sub_perks[1]["perk"]), False)["name"],
                        offense_perk=participant["perks"]["statPerks"]["offense"],
                        flex_perk=participant["perks"]["statPerks"]["flex"],
                        defense_perk=participant["perks"]["statPerks"]["offense"],
                    )
                    self.riot_repository.save_participant(db_participant)

                last_match_time = game_end_at

            self.riot_repository.update_summoner(summoner.puuid, last_match_time)

            if len(matches) < 100:
                break
