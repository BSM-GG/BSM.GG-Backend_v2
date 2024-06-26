class InvalidAuthorizationCode(Exception):
    def __init__(self, auth_code: str):
        self.auth_code: str = auth_code


class AlreadyExistUser(Exception):
    def __init__(self, username: str):
        self.username: str = username


class InvalidToken(Exception):
    def __init__(self, token: str):
        self.token: str = token


class RiotAPIForbidden(Exception):
    def __init__(self):
        pass


class SummonerNotFoundByRiotAPI(Exception):
    def __init__(self, game_name: str, tag_line: str):
        self.game_name: str = game_name
        self.tag_line: str = tag_line


class SummonerNotFound(Exception):
    def __init__(self, game_name: str, tag_line: str):
        self.game_name: str = game_name
        self.tag_line: str = tag_line


class NoVPN(Exception):
    def __init__(self):
        pass
