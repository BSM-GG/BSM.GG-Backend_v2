import json
import os

import requests
from dotenv import load_dotenv

from repository.riot.riot_repository import RiotRepository

load_dotenv()


class RiotGetService:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.kr_url = os.getenv("KR_URL")
        self.asia_lol_url = os.getenv("ASIA_LOL_URL")
        self.asia_riot_url = os.getenv("ASIA_RIOT_URL")

        self.riot_repository = RiotRepository()

    async def get_riot_account(self, game_name: str, tag_line: str):
        response = requests.get(
            f"{self.asia_riot_url}/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={self.api_key}"
        )
        return response.json()

    async def get_summoner(self, game_name: str, tag_line: str):
        puuid = await self.riot_repository.get_summoner_by_name_and_tag(game_name, tag_line)
        return puuid

    async def get_summoner_info(self, puuid: str):
        response = requests.get(
            f"{self.kr_url}/summoner/v4/summoners/by-puuid/{puuid}?api_key={self.api_key}"
        )
        return json.loads(response.text)

    async def get_rank_info(self, id: str):
        response = requests.get(f"{self.kr_url}/league/v4/entries/by-summoner/{id}?api_key={self.api_key}")
        return json.loads(response.text)

    async def get_matches(self, puuid: str, start_time: int):
        response = requests.get(f"{self.asia_lol_url}/match/v5/matches/by-puuid/{puuid}/ids?startTime={start_time}&start=0&count=100&api_key={self.api_key}")
        return json.loads(response.text)

    async def get_match_data(self, match_id: str):
        response = requests.get(f"{self.asia_lol_url}/match/v5/matches/{match_id}?api_key={self.api_key}")
        return json.loads(response.text)
