from pydantic import BaseModel


class UserRequestModel(BaseModel):
    auth_code: str


class JwtModel(BaseModel):
    token: str
    game_name: str
    tag_line: str
