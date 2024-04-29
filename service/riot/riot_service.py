import json
import os
import requests
from dotenv import load_dotenv

from repository.riot.riot_repository import RiotRepository
from repository.user.user_repository import UserRepository

load_dotenv()


class RiotService:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.kr_url = os.getenv("KR_URL")
        self.asia_url = os.getenv("ASIA_URL")

        self.riot_repository = RiotRepository()
        self.user_repository = UserRepository()

    async def get_riot_account(self, game_name: str, tag_line: str):
        response = requests.get(
            f"{self.asia_url}/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={self.api_key}"
        )
        return response.json()

    async def get_summoner_info(self, puuid: str):
        response = requests.get(
            f"{self.kr_url}/summoner/v4/summoners/by-puuid/{puuid}?api_key={self.api_key}"
        )
        return json.loads(response.text)

    async def get_rank_info(self, id: str):
        response = requests.get(f"{self.kr_url}/league/v4/entries/by-summoner/{id}?api_key={self.api_key}")
        return json.loads(response.text)

    async def create_summoner(self, puuid: str, game_name, tag_line):
        summoner_info = await self.get_summoner_info(puuid)
        rank_info = await self.get_rank_info(summoner_info["id"])

        rank_info = rank_info[["queueType"] == "RANKED_SOLO_5x5"]
        self.riot_repository.save(summoner_info, rank_info, game_name, tag_line)
