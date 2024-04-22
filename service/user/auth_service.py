import os
import requests


class AuthService:

    def __init__(self):
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')

    async def get_token(self, client, auth_code: str):
        response = requests.get('https://auth.bssm.kro.kr/api/oauth',
                                params={
                                    "client_id": self.client_id,
                                    "client_secret": self.client_secret,
                                    "auth_code": auth_code
                                })
        # response = client.post("https://auth.bssm.kro.kr/api/oauth",
        #                              json={
        #                                  "client_id": self.client_id,
        #                                  "client_secret": self.client_secret,
        #                                  "auth_code": auth_code
        #                              })
        return response.json().get('token')

    async def get_user(self, client, token):
        response = client.post("https://auth.bssm.kro.kr/api/oauth",
                               json={
                                   "client_id": self.client_id,
                                   "client_secret": self.client_secret,
                                   "token": token
                               })
        return response
