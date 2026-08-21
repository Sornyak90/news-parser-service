from contextlib import asynccontextmanager

from database import init_db
from fastapi import FastAPI
from models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):

    engine, _ = init_db()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()
