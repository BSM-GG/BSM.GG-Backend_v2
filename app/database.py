from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

user_name = os.getenv('USER_NAME')
user_pw = os.getenv('USER_PW')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')


engine = create_engine(
    f'mysql://{user_name}:{user_pw}@{db_host}/{db_name}?charset=utf8mb4',
    pool_pre_ping=True,
    pool_size=10,
    pool_recycle=3600,
    max_overflow=20,
    # echo=True
)
SessionLocal = sessionmaker(
    bind=engine,
)

Base = declarative_base()


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
