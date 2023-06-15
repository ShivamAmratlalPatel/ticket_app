"""Schemas for the API."""
from pydantic import BaseModel


class ChapterList(BaseModel):
    """Schema for the list of chapters."""

    chapters: list = []

    class Config:
        """Pydantic configuration."""

        schema_extra = {
            "example": {
                "chapters": [
                    "Chapter 1",
                    "Chapter 2",
                    "Chapter 3",
                ],
            },
        }
