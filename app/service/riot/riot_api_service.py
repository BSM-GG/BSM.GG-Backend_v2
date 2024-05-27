import json
import os

import requests
from dotenv import load_dotenv

from app.utility.error.errors import NoVPN

load_dotenv()


class RiotAPIService:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.kr_url = os.getenv("KR_URL")
        self.asia_lol_url = os.getenv("ASIA_LOL_URL")
        self.asia_riot_url = os.getenv("ASIA_RIOT_URL")

    async def get_riot_account_by_riotAPI(self, game_name: str, tag_line: str):
        try:
            response = requests.get(
                f"{self.asia_riot_url}/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={self.api_key}"
            )
            return json.loads(response.text)
        except Exception:
            raise NoVPN()

    async def get_riot_account_by_puuid(self, puuid: str):
        try:
            response = requests.get(
                f"{self.asia_riot_url}/account/v1/accounts/by-puuid/{puuid}?api_key={self.api_key}"
            )
            return json.loads(response.text)
        except Exception:
            raise NoVPN()

    async def get_summoner_info_by_riotAPI(self, puuid: str):
        try:
            response = requests.get(
                f"{self.kr_url}/summoner/v4/summoners/by-puuid/{puuid}?api_key={self.api_key}"
            )
            return json.loads(response.text)
        except Exception:
            raise NoVPN()

    async def get_rank_info_by_riotAPI(self, id: str):
        try:
            response = requests.get(f"{self.kr_url}/league/v4/entries/by-summoner/{id}?api_key={self.api_key}")
            return json.loads(response.text)
        except Exception:
            raise NoVPN()

    async def get_matches_by_riotAPI(self, puuid: str, start_time: int):
        try:
            response = requests.get(
                f"{self.asia_lol_url}/match/v5/matches/by-puuid/{puuid}/ids?startTime={start_time}&start=0&count=100&api_key={self.api_key}")
            return json.loads(response.text)
        except Exception:
            raise NoVPN()

    async def get_match_data_by_riotAPI(self, match_id: str):
        try:
            response = requests.get(f"{self.asia_lol_url}/match/v5/matches/{match_id}?api_key={self.api_key}")
            return json.loads(response.text)
        except Exception:
            raise NoVPN()
