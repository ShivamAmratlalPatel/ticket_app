"""Schemas for the API."""
from pydantic import BaseModel


class ChapterList(BaseModel):
    chapters: list = []

    class Config:
        schema_extra = {
            "example": {
                "chapters": [
                    "Chapter 1",
                    "Chapter 2",
                    "Chapter 3",
                ]
            }
        }
