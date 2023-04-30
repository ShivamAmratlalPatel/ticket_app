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
