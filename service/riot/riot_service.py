import json
import os
import requests
from dotenv import load_dotenv

from domain.tables import Participant
from repository.riot.riot_repository import RiotRepository
from repository.user.user_repository import UserRepository
from service.riot.mapping.name_mapping import QUEUE_TYPE, PERKS, SPELL_NAME
from service.riot.riot_get_service import RiotGetService

load_dotenv()


class RiotService:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.kr_url = os.getenv("KR_URL")
        self.asia_url = os.getenv("ASIA_URL")
        self.season_started_time = os.getenv("SEASON_STARTED_TIME")

        self.riot_get_service = RiotGetService()
        self.user_get_service = UserRepository()
        self.riot_repository = RiotRepository()
        self.user_repository = UserRepository()
        # const QUEUETYPE = {
        #     440: 'flex',
        #     900: 'urf',
        #     920: 'poro',
        #     1020: 'ofa',
        #     1300: 'nbg',
        #     1400: 'usb', // Ultimate Spellbook
        #     2000: 'tut',
        #     2010: 'tut',
        #     2020: 'tut',
        # }


    async def create_summoner(self, puuid: str, game_name: str, tag_line: str):
        summoner_info = await self.riot_get_service.get_summoner_info(puuid)
        rank_info = await self.riot_get_service.get_rank_info(summoner_info["id"])

        rank_info = rank_info[["queueType"] == "RANKED_SOLO_5x5"]
        self.riot_repository.save(summoner_info, rank_info, game_name, tag_line)

    async def update_record(self, game_name: str, tag_line: str):

        summoner = await self.riot_get_service.get_summoner(game_name, tag_line)
        if not summoner:
            return {
                "code": "404",
                "message": "Cannot Find Summoner"
            }

        matches = await self.riot_get_service.get_matches(summoner["puuid"], summoner["last_updated"])
        while True:
            if len(matches) == 0:
                return
            for match_id in matches:
                match = await self.riot_get_service.get_match_data(match_id)
                # match info
                game_start_at = match["info"]["gameCreation"]
                game_end_at = match["info"]["gameEndTimestamp"]
                game_duration = match["info"]["gameDuration"]
                game_type = QUEUE_TYPE[match["info"]["queueId"]]
                self.riot_repository.save_match(match_id, game_start_at, game_end_at, game_duration, game_type)

                participants = match["info"]["participants"]
                for participant in participants:
                    participant_puuid = participant["puuid"]
                    win = participant["win"]
                    champion = participant["championName"]
                    champion_level = participant["champLevel"]
                    lane = participant["lane"]
                    kill = participant["kills"]
                    assist = participant["assists"]
                    death = participant["deaths"]
                    cs = participant["totalMinionsKilled"]
                    damage = participant["totalDamageDealt"]
                    damage_rate = round(participant["damageTakenOnTeamPercentage"]*100)
                    gain_damage = participant["totalDamageTaken"]
                    heal = participant["totalHeal"]
                    vision_ward = participant["visionWardsBoughtInGame"]
                    sight_ward = participant["sightWardsBoughtInGame"]
                    vision_score = participant["sightWardsBoughtInGame"]
                    spell1 = SPELL_NAME[participant["summoner1Id"]]
                    spell2 = SPELL_NAME[participant["summoner2Id"]]
                    item1 = participant["item0"]
                    item2 = participant["item1"]
                    item3 = participant["item2"]
                    item4 = participant["item3"]
                    item5 = participant["item4"]
                    item6 = participant["item5"]
                    ward = participant["item6"]
                    main_perk = PERKS[["id" == participant["perks"]["styles"][["description" == "primaryStyle"]]["selections"][0]["perk"]]]["name"]
                    main_perk_part1 = PERKS[["id" == participant["perks"]["styles"][["description" == "primaryStyle"]]["selections"][1]["perk"]]]["name"]
                    main_perk_part2 = PERKS[["id" == participant["perks"]["styles"][["description" == "primaryStyle"]]["selections"][2]["perk"]]]["name"]
                    main_perk_part3 = PERKS[["id" == participant["perks"]["styles"][["description" == "primaryStyle"]]["selections"][3]["perk"]]]["name"]
                    sub_perk = PERKS[["id" == participant["perks"]["styles"][["description" == "subStyle"]]["selections"][0]["perk"]]]["name"]
                    sub_perk_part1 = PERKS[["id" == participant["perks"]["styles"][["description" == "subStyle"]]["selections"][1]["perk"]]]["name"]
                    sub_perk_part2 = PERKS[["id" == participant["perks"]["styles"][["description" == "subStyle"]]["selections"][2]["perk"]]]["name"]
                    offense_perk = participant["perks"]["statPerks"]["offense"]
                    flex_perk = participant["totalMinionsKilled"]["flex"]
                    defense_perk = participant["totalMinionsKilled"]["defense"]
                    # 반복되는건 리스트로
                    db_participant = Participant(
                        puuid=participant["puuid"],
                        match_id=match_id,
                        win=participant["win"],
                        champion=participant["champion"],
                        champion_level=participant["championLevel"],
                        lane=participant["lane"],
                        kill=participant["kills"],
                        assist=participant["assists"],
                        death=participant["deaths"],
                        cs=participant["totalMinionsKilled"],
                        damage=participant["totalDamageTaken"],
                        damage_rate=round(participant["damageTakenOnTeamPercentage"]*100),
                        gain_damage=participant["totalDamageTaken"],
                        heal=participant["totalHeal"],
                        vision_ward=participant["visionWardsBoughtInGame"],
                        sight_ward=participant["sightWardsBoughtInGame"],
                        vision_score=participant["sightWardsBoughtInGame"],
                        spell1=spell1,
                        spell2=spell2,
                        main_perk=main_perk,
                        main_perk_part1=main_perk_part1,
                        main_perk_part2=main_perk_part2,
                        main_perk_part3=main_perk_part3,
                        sub_perk=sub_perk,
                        sub_perk_part1=sub_perk_part1,
                        sub_perk_part2=sub_perk_part2,
                        offense_perk=offense_perk,
                        flex_perk=flex_perk,
                        defense_perk=defense_perk,
                    )
                    self.riot_repository.save_participant(db_participant)

                    summoner

        return matches

#                 "item0": 6655,
#                 "item1": 4628,
#                 "item2": 3020,
#                 "item3": 4645,
#                 "item4": 3089,
#                 "item5": 3137,
#                 "item6": 2052,
