"""Main module for the FastAPI application."""

from fastapi import FastAPI, status, Depends, HTTPException

from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .helpers import get_db
from .models import Chapter
from .schemas import ChapterList

app = FastAPI()

# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=dict, status_code=status.HTTP_200_OK)
async def root() -> dict[str, str]:
    """
    Root endpoint for the API.

    Returns:
        dict: message

    Examples:
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

    Returns:
        dict: status

    Examples
        >>> healthcheck()
        {"status": "ok"}
    """
    return {"status": "ok"}


@app.get(
    "/chapters",
    status_code=status.HTTP_200_OK,
    response_model=ChapterList,
    tags=["chapters"],
    summary="Get a list of chapters.",
    description="Get a list of chapters.",
    responses={
        status.HTTP_200_OK: {
            "description": "List of chapters.",
            "content": {
                "application/json": {
                    "example": {"chapters": ["Chapter 1", "Chapter 2", "Chapter 3"]}
                }
            },
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Unable to retrieve chapters from the database.",
            "content": {"application/json": {"example": {"detail": str}}},
        },
    },
)
def get_chapters(db: Session = Depends(get_db)) -> ChapterList:
    """
    Get a list of chapters.

    Args:
        db: Session
            database session

    Returns:
        ChapterList: list of chapters

    Raises:
        HTTPException: if unable to retrieve chapters from the database

    Examples:
        >>> get_chapters()
        ChapterList(chapters=["Chapter 1", "Chapter 2", "Chapter 3"])
    """
    try:
        chapters = db.query(Chapter.chapter_name).all()
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to retrieve chapters from the database.",
        )
    return ChapterList(chapters=[chapter[0] for chapter in chapters])
