"""Main module for the FastAPI application."""

from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Query, Session

from src.helpers import get_db
from src.models import Chapter
from src.schemas import ChapterList

app = FastAPI()

# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Depends(get_db)


@app.get("/", response_model=dict, status_code=status.HTTP_200_OK)
async def root() -> dict[str, str]:
    """
    Root endpoint for the API.

    Returns
    -------
        dict: message

    Examples
    --------
        >>> root()
        {"message": "Hello World"}

    """
    return {"message": "Hello World"}


@app.get("/hello/{name}", response_model=dict, status_code=status.HTTP_200_OK)
async def say_hello(name: str) -> dict[str, str]:
    """
    Say hello to the user.

    Args:
        name: str
            name to say hello to

    Returns:
        dict: message

    Examples:
        >>> say_hello("John")
        {"message": "Hello John"}
    """
    return {"message": f"Hello {name}"}


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def healthcheck() -> dict[str, str]:
    """
    Healthcheck endpoint for the API.

    Returns
    -------
        dict: status

    Examples
    --------
        >>> healthcheck()
        {"status": "ok"}
    """
    return {"status": "ok"}


@app.get(
    "/chapters",
    response_model=ChapterList,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ChapterList,
            "description": "Chapters not found",
        },
    },
)
def get_chapters(db: Session = db) -> ChapterList:
    """
    Get a list of chapters.

    Args:
        db: Session

    Returns:
        ChapterList: list of chapters

    Raises:
        HTTPException: if unable to retrieve chapters from the database

    Examples:
        >>> get_chapters()
    """
    chapters: Query[type[Chapter]] = db.query(Chapter)

    chapters = [chapter.chapter_name for chapter in chapters]

    return ChapterList(chapters=chapters)
