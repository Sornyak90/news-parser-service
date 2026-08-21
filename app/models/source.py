from datetime import datetime

from models import Base
from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Identity, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Source(Base):
    __tablename__ = "source"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    url: Mapped[str] = mapped_column(String, unique=True)
    topic: Mapped[str] = mapped_column(String(100))
    priority: Mapped[int] = mapped_column(Integer, default=5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    last_parsed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class SourceCreate(BaseModel):
    url: str
    topic: str


class SourceResponse(BaseModel):
    id: int
    url: str
    topic: str
    priority: int
    is_active: bool
    created_at: datetime
