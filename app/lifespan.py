from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.database import Base, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):

    engine, session_maker = init_db()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()
  
