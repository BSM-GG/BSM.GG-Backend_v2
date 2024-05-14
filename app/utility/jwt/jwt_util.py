import os

import jwt
from dotenv import load_dotenv

from fastapi.security import OAuth2PasswordBearer, APIKeyHeader

from app.service.user.user_get_service import UserGetService
from app.utility.error.errors import InvalidToken

load_dotenv()


class JwtUtil:

    def __init__(self):
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
        self.secret_key = os.getenv("SECRET_KEY")
        self.algorithm = os.getenv("ALGORITHM")
        self.api_key_header = APIKeyHeader(name="Token")

        self.user_get_service = UserGetService()

    def create_token(self, username: str) -> str:
        to_encode = {
            "uuid": username
        }
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def decode_token(self, authorization: str):
        try:
            bearer, token = authorization.split(" ")
            if not token or bearer.lower() != "bearer":
                raise InvalidToken(authorization)
        except Exception:
            raise InvalidToken(authorization)
        payload = jwt.decode(token.replace('"', ''), self.secret_key, self.algorithm)
        user = self.user_get_service.get_user_by_uuid(payload['uuid'])
        return user
