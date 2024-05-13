from pydantic import BaseModel


class SummonerModel(BaseModel):
    game_name: str
    tag_line: str
