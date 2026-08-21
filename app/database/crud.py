from models.source import Source, SourceCreate
from sqlalchemy.ext.asyncio import AsyncSession


async def create_source(source_data: SourceCreate, get_session: AsyncSession):
    async with get_session as session:
        row = Source(url=source_data.url, topic=source_data.topic)
        session.add(row)
        await session.commit()
        await session.refresh(row)
        return row


# get_all_sources(db) — возвращает все источники

# get_source_by_id(db, source_id) — возвращает один источник по ID
