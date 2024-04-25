from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controller.user.user_controller import user_controller
from domain.user.user_table import Base
from database import SessionLocal, engine

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(user_controller)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
