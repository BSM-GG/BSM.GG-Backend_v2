from dotenv import load_dotenv

from app.repository.riot.riot_repository import RiotRepository

load_dotenv()


class RiotGetService:

    def __init__(self):
        self.riot_repository = RiotRepository()

    async def get_summoner_by_game_name_and_tag_line(self, game_name: str, tag_line: str):
        return await self.riot_repository.find_summoner_by_name_and_tag(game_name, tag_line)

    async def get_summoner_by_puuid(self, puuid: str):
        return await self.riot_repository.find_summoner_by_puuid(puuid)

    async def get_match(self, match_id: str):
        return await self.riot_repository.find_match_by_id(match_id)

    async def get_participant_by_puuid_and_match_id(self, puuid: str, match_id: str):
        return await self.riot_repository.find_participant_by_ids(puuid, match_id)

    async def get_matches_by_puuid(self, puuid: str, offset: int, limit: int):
        return await self.riot_repository.find_matches_by_puuid(puuid, offset, limit)

    async def get_participant_in_match(self, match_id):
        return await self.riot_repository.find_participant_in_match(match_id)
