from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class Feed(Base):
    __tablename__ = "feed"

    id: Mapped[int] = mapped_column(primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"), index=True)
    telegram_message_id: Mapped[int] = mapped_column(Integer, nullable=True)
    chat_id: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    error_text: Mapped[str] = mapped_column(Text, nullable=True)
    sent_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
