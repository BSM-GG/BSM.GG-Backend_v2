from pydantic import BaseModel


class UserRiotAccount(BaseModel):
    puuid: str
    game_name: str
    tag_line: str
