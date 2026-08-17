import uvicorn
from fastapi import FastAPI

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


if __name__ == "__main__":
    uvicorn.run(
        "main:my_app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="warning",
    )