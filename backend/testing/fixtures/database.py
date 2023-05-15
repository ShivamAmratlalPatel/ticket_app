import os

import pytest
from sqlalchemy import MetaData

from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from src.database import session_local_factory  # noqa F401


@pytest.fixture(scope="session")
def session_factory():
    # Migrate the database if it's not up to date.
    database_url = os.environ["DATABASE_URL"]
    if database_url != "postgresql://nhsf@postgres/nhsf_backend":
        exit(1)
    alembic_config = AlembicConfig("alembic.ini")
    alembic_config.set_main_option("sqlalchemy.url", database_url)
    alembic_upgrade(alembic_config, "head")

    session_factory = session_local_factory(database_url)

    # import logging
    # logging.basicConfig()
    # logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    return session_factory


@pytest.fixture(scope="function")
def session(session_factory):
    sess = session_factory()
    engine = session_factory.kw["bind"]
    meta = MetaData()
    meta.reflect(bind=engine)
    conn = engine.connect()
    transaction = conn.begin()
    for table in meta.sorted_tables:
        if table.name in [
            "alembic_version",
        ]:
            continue
        conn.execute(f"TRUNCATE {table.name} CASCADE")
    transaction.commit()

    try:
        yield sess
    except Exception:
        raise
    finally:
        sess.close()
