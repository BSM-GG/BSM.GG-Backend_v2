from pydantic import BaseModel


class UserRequestModel(BaseModel):
    auth_code: str


class JwtModel(BaseModel):
    token: str
