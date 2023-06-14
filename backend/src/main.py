"""Main module for the FastAPI application."""

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

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


# @app.get(
#     "/chapters",
#         status.HTTP_200_OK: {
#                 "application/json": {
#             },
#         },
#         status.HTTP_500_INTERNAL_SERVER_ERROR: {
#         },
#     },
# def get_chapters(db: Session = Depends(get_db)) -> ChapterList:
#     """
#     Get a list of chapters.
#
#     Args:
#             database session
#
#     Returns:
#         ChapterList: list of chapters
#
#     Raises:
#         HTTPException: if unable to retrieve chapters from the database
#
#     Examples:
#         >>> get_chapters()
#     """
#         raise HTTPException(


@app.get("/hihihih", status_code=status.HTTP_200_OK)
def hi() -> dict[str, str]:
    """
    Say hi to the user.

    Returns
    -------
        dict: message

    Examples
    --------
        >>> hi()
        {"message": "Hi there!"}
    """
    return {"message": "Hi there!"}
