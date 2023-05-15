"""Generate a UUID"""
from uuid import uuid4, UUID


def generate_uuid() -> UUID:
    """
    Generate a UUID

    Returns:
        UUID: A UUID

    Example:
        >>> generate_uuid()
        UUID('e4eaaaf2-d142-11e1-b3e4-080027620cdd')
    """

    return uuid4()
