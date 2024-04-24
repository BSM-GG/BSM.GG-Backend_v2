from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os


user_name = os.getenv('USER_NAME')
user_pw = os.getenv('USER_PW')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

DATABASE = f'mysql://{user_name}:{user_pw}@{db_host}/{db_name}?charset=utf8'

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()