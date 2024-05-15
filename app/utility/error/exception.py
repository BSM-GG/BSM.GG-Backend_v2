from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse

from app.utility.error.errors import InvalidAuthorizationCode, AlreadyExistUser, InvalidToken, \
    SummonerNotFoundByRiotAPI, \
    RiotAPIForbidden, SummonerNotFound, NoVPN


def add_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def request_validation_handler(request: Request, exc):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status_code": 400,
                "message": "invalid request format"
            }
        )

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, exc):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": 500,
                "message": "internal server error"
            }
        )

    @app.exception_handler(InvalidAuthorizationCode)
    async def invalid_authorization_code_exception_handler(request: Request, exc: InvalidAuthorizationCode):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "status_code": 403,
                "message": "Invalid Authorization Code",
                "auth_code": exc.auth_code
            }
        )

    @app.exception_handler(AlreadyExistUser)
    async def already_exist_exception_handler(request: Request, exc: AlreadyExistUser):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "status_code": 409,
                "message": "Already Exist User",
                "username": exc.username
            }
        )

    @app.exception_handler(InvalidToken)
    async def already_exist_exception_handler(request: Request, exc: InvalidToken):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "status_code": 403,
                "message": "Invalid Token",
                "token": exc.token
            }
        )

    @app.exception_handler(RiotAPIForbidden)
    async def already_exist_exception_handler(request: Request, exc: SummonerNotFoundByRiotAPI):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "status_code": 403,
                "message": "Riot API Occur Forbidden",
            }
        )

    @app.exception_handler(SummonerNotFoundByRiotAPI)
    async def already_exist_exception_handler(request: Request, exc: SummonerNotFoundByRiotAPI):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status_code": 404,
                "message": "Summoner Not Found By Riot API",
                "game_name": exc.game_name,
                "tag_line": exc.tag_line,
            }
        )

    @app.exception_handler(SummonerNotFound)
    async def already_exist_exception_handler(request: Request, exc: SummonerNotFound):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status_code": 404,
                "message": "Summoner Not Found",
                "game_name": exc.game_name,
                "tag_line": exc.tag_line,
            }
        )

    @app.exception_handler(NoVPN)
    async def already_exist_exception_handler(request: Request, exc: NoVPN):
        return JSONResponse(
            status_code=status.HTTP_418_IM_A_TEAPOT,
            content={
                "status_code": 418,
                "message": "Something Goes Wrong...",
            }
        )