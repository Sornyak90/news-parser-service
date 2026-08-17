from sqlalchemy.orm import declarative_base

from .source import Source
from .article import Article
from .feed import Feed

Base = declarative_base()