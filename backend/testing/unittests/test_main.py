"""Test the main module."""

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.src import app, get_db
from backend.src.commands import generate_uuid
from backend.src.models import Chapter
from testing.fixtures.database import session, session_factory  # noqa: F401


@pytest.fixture()
def client(session: Session) -> TestClient:  # noqa: F811
    """
    Get a test client for the FastAPI app.

    Returns
        TestClient: test client for the FastAPI app

    """
    app.dependency_overrides[get_db] = lambda: session
    return TestClient(app)


def test_root(client: TestClient) -> None:
    """
    Test the root endpoint.

    Args:
        client: TestClient

    Returns:
        None
    """
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}


def test_hello(client: TestClient) -> None:
    """
    Test the hello endpoint.

    Args:
        client: TestClient

    Returns:
        None
    """
    response = client.get("/hello/John")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello John"}


def test_healthcheck(client: TestClient) -> None:
    """
    Test the healthcheck endpoint.

    Args:
        client: TestClient

    Returns:
        None
    """
    response = client.get("/healthcheck")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}


def test_get_chapters(client: TestClient, session: Session) -> None:  # noqa: F811
    """
    Test the get_chapters endpoint.

    Args:
        client: TestClient
        session: Session

    Returns:
        None
    """
    chapter = Chapter(
        chapter_id=generate_uuid(),
        chapter_name="Chapter 1",
        is_deleted=False,
    )
    session.add(chapter)
    chapter = Chapter(
        chapter_id=generate_uuid(),
        chapter_name="Chapter 2",
        is_deleted=False,
    )
    session.add(chapter)
    chapter = Chapter(
        chapter_id=generate_uuid(),
        chapter_name="Chapter 3",
        is_deleted=False,
    )
    session.add(chapter)
    session.commit()
    response = client.get("/chapters")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"chapters": ["Chapter 1", "Chapter 2", "Chapter 3"]}
