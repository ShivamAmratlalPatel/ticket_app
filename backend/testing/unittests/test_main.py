"""Test the main module."""

import pytest
from fastapi.testclient import TestClient

from src import app  # noqa: F401
from src import get_db  # noqa: F401

from backend.testing.fixtures.database import session  # noqa: F401

client = TestClient(app)


@pytest.mark.parametrize(
    "endpoint, expected_status_code, expected_response",
    [
        ("/", 200, {"message": "Hello World"}),
        ("/hello/John", 200, {"message": "Hello John"}),
        ("/healthcheck", 200, {"status": "ok"}),
    ],
)
def test_main_endpoints(
    endpoint: str, expected_status_code: int, expected_response: dict
) -> None:
    """
    Test the main endpoints.

    Args:
        endpoint: str
            endpoint to test
        expected_status_code: int
            expected status code
        expected_response: dict
            expected response

    Returns:
        None
    """
    response = client.get(endpoint)
    assert response.status_code == expected_status_code
    assert response.json() == expected_response


def test_get_chapters():
    """
    Test the get_chapters endpoint.

    Returns:
        None
    """
    response = client.get("/chapters")
    assert response.status_code == 200
    assert response.json() == ["Chapter 1", "Chapter 2", "Chapter 3"]
