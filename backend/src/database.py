"""File for storing database connection functions"""
import os

from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool


def session_local_factory(database_url: str = None) -> sessionmaker[Session]:
    if database_url is None:
        database_url = os.environ["DATABASE_URL"]
    engine: Engine = create_engine(database_url, poolclass=NullPool)
    session_factory: sessionmaker[Session] = sessionmaker(bind=engine)

    return session_factory


Base = declarative_base()
