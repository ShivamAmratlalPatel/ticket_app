"""Helper functions for the FastAPI app."""
from .database import session_local_factory


def get_db() -> None:
    """
    Get a database session.

    Returns
    -------
        None
    """
    db = session_local_factory()()
    try:
        yield db
    finally:
        db.close()
