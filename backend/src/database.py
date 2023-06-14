"""File for storing database connection functions."""
import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import NullPool


def session_local_factory(database_url: str | None = None) -> sessionmaker[Session]:
    """
    Create a session factory for a local database.

    Args:
        database_url (str, optional): database URL. Defaults to None.
    ----


    Returns:
    -------
        sessionmaker[Session]: session factory

    """
    if database_url is None:
        database_url = os.environ["DATABASE_URL"]
    engine: Engine = create_engine(database_url, poolclass=NullPool)
    session_factory: sessionmaker[Session] = sessionmaker(bind=engine)

    return session_factory


Base = declarative_base()
