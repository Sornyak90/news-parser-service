from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import AsyncAdaptedQueuePool

from app.config import settings

_engine = None
_session_maker = None


def init_db(engine=None):
    """Инициализация БД."""
    global _engine, _session_maker

    if engine is None:
        _engine = create_async_engine(
            url=(
                f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}"
                f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
            ),
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
            pool_recycle=3600,
            pool_pre_ping=True,
            poolclass=AsyncAdaptedQueuePool,
        )
    else:
        _engine = engine

    _session_maker = async_sessionmaker(
        _engine, expire_on_commit=False, autocommit=False, autoflush=False
    )
    return _engine, _session_maker


def get_session():
    """Получение сессии."""
    if _session_maker is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    return _session_maker()


def get_engine():
    """Получение engine."""
    if _engine is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    return _engine
