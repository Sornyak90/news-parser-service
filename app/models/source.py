from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import String, Integer, Boolean, DateTime
from app.models import Base


class Source(Base):
    __tablename__ = "source"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String, unique=True)
    topic: Mapped[str] = mapped_column(String(100))
    priority: Mapped[int] = mapped_column(Integer, default=5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    last_parsed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
