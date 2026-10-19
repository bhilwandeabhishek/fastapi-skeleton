# FastAPI application entry point.
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import settings
from src.api.v1.router import router as v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic goes here.
    print(f"Starting {settings.APP_NAME}")

    yield

    # Shutdown / cleanup logic goes here.
    print(f"Stopping {settings.APP_NAME}")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Reusable FastAPI application skeleton",
    debug=settings.DEBUG,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    return {
        "message": "Welcome to the FastAPI application",
        "docs": "/docs",
        "health": "/api/v1/health",
    }


app.include_router(
    v1_router,
    prefix=settings.API_V1_PREFIX,
)
