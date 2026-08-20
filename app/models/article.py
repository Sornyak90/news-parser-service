from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(500))
    url: Mapped[str] = mapped_column(String(1000), unique=True)
    summary: Mapped[str] = mapped_column(Text, nullable=True)
    published_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    content_hash: Mapped[str] = mapped_column(String(32), unique=True)
    source_id: Mapped[int] = mapped_column(ForeignKey("source_id.id"), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
