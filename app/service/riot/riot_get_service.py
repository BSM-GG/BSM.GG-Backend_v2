from dotenv import load_dotenv

from app.repository.riot.riot_repository import RiotRepository

load_dotenv()


class RiotGetService:

    def __init__(self):
        self.riot_repository = RiotRepository()

    async def find_summoner(self, game_name: str, tag_line: str):
        return await self.riot_repository.find_summoner_by_name_and_tag(game_name, tag_line)

    async def find_match(self, match_id: str):
        return self.riot_repository.find_match_by_id(match_id)

    async def find_participant(self, puuid: str, match_id: str):
        return self.riot_repository.find_participant_by_ids(puuid, match_id)
