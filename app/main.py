import uvicorn
from fastapi import FastAPI

from app.api.v1.sources import router as sources_router
from app.config import settings

from . import lifespan

# Создание приложения
my_app = FastAPI(
    title="TaskBD",
    version="2.33.5",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

my_app.include_router(sources_router, prefix="/api/v1/sources", tags=["sources"])

if __name__ == "__main__":
    uvicorn.run(
        "main:my_app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="warning",
    )
