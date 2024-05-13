import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class AuthService:

    def __init__(self):
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')

    async def get_token(self, auth_code: str):
        response = requests.post(
            'https://auth.bssm.kro.kr/api/oauth/token',
            json={
                "clientId": self.client_id,
                "clientSecret": self.client_secret,
                "authCode": auth_code
            }
        )
        return response.json().get('token')

    async def get_user(self, token):
        response = requests.post(
            'https://auth.bssm.kro.kr/api/oauth/resource',
            json={
                "clientId": self.client_id,
                "clientSecret": self.client_secret,
                "token": token
            }
        )
        user = json.loads(response.text)["user"]
        if user["role"] == "TEACHER":
            user["isGraduate"] = False
            user["enrolledAt"] = 0
            user["grade"] = 0
            user["classNo"] = 0
            user["studentNo"] = 0
        return user

