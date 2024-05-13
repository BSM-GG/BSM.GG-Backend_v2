import os

import jwt
from dotenv import load_dotenv

from fastapi.security import OAuth2PasswordBearer

load_dotenv()


class JwtUtil:

    def __init__(self):
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
        self.secret_key = os.getenv("SECRET_KEY")
        self.algorith = os.getenv("ALGORITHM")

    def create_token(self, username: str) -> str:
        to_encode = {
            "uuid": username
        }
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorith)
        return encoded_jwt

    def decode_token(self, token):
        pass