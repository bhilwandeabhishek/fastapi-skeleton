# FastAPI router for health check endpoints.

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    """Check whether the API is responding."""
    return {
        "status": "ok",
        "message": "API is healthy",
    }


@router.get("/health/ready", tags=["Health"])
async def readiness_check() -> dict[str, str]:
    """Check whether the application is ready to serve requests."""
    return {
        "status": "ready",
    }
