import os
import requests


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
        print(response.json())
        return response.json().get('token')

    async def get_user(self, token):
        # response = client.post("https://auth.bssm.kro.kr/api/oauth",
        #                        json={
        #                            "client_id": self.client_id,
        #                            "client_secret": self.client_secret,
        #                            "token": token
        #                        })
        response = requests.post('https://auth.bssm.kro.kr/api/oauth/resource',
                                json={
                                    "clientId": self.client_id,
                                    "clientSecret": self.client_secret,
                                    "token": token
                                })
        return response.json()
