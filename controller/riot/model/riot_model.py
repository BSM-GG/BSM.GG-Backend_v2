from pydantic import BaseModel


class MatchesCreate(BaseModel):
    game_name: str
    tag_line: str
