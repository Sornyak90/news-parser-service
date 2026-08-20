from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .article import Article
from .feed import Feed
from .source import Source

__all__ = ["Article", "Base", "Feed", "Source"]
