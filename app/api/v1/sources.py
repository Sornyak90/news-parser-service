from datetime import datetime

from database.crud import create_source
from database.session import get_session
from fastapi import APIRouter, Depends
from models.source import SourceCreate, SourceResponse
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/", response_model=SourceResponse)
async def create_source(
    source: SourceCreate, session: AsyncSession = Depends(get_session)
) -> SourceResponse:
    # Заглушка: возвращаем данные без сохранения в БД
    return create_source(source, session)


@router.get("/")
async def get_all_sources():
    return {"source": []}


@router.get("/{id}")
async def get_source_by_id(db, source_id):
    pass
