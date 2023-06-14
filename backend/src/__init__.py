"""Main module for the FastAPI application."""
from .database import Base
from .helpers import get_db
from .main import app
from .models import Chapter
