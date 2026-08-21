import uvicorn
from api.v1.sources import router as sources_router
from config import settings
from fastapi import FastAPI
from lifespan import lifespan

# Создание приложения
app = FastAPI(
    title="NewsPublic",
    version="2.33.5",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.include_router(sources_router, prefix="/api/v1/sources", tags=["sources"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="warning",
    )
