from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse

from app.utility.error.errors import InvalidAuthorizationCode, AlreadyExistUser


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