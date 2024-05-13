class InvalidAuthorizationCode(Exception):
    def __init__(self, auth_code: str):
        self.auth_code: str = auth_code


class AlreadyExistUser(Exception):
    def __init__(self, username: str):
        self.username: str = username