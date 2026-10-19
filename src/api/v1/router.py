# FastAPI router for health check endpoints.
from src.users.routes import router as users_router
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

#router for users endpoints.
router.include_router(
    users_router, 
    prefix="/users", 
    tags=["Users"]
)