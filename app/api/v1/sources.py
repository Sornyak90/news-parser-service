from datetime import UTC, datetime

from fastapi import APIRouter

from app.models.source import SourceCreate, SourceResponse

router = APIRouter()


@router.get("/")
async def get_all_sources():
    return {"source": []}


@router.post("/", response_model=SourceResponse)
async def create_source(source: SourceCreate):
    # Заглушка: возвращаем данные без сохранения в БД
    return SourceResponse(
        id=1,
        url=source.url,
        topic=source.topic,
        priority=5,
        is_active=True,
        created_at=datetime.now(UTC),
    )
