import logging
from typing import Any

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.common.exceptions import ApplicationError
from src.common.responses import error_response

logger = logging.getLogger(__name__)


async def application_error_handler(
    request: Request,
    exc: ApplicationError,
) -> JSONResponse:
    logger.debug("Handling %s for %s %s", exc.code, request.method, request.url.path)
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(exc.code, exc.message),
    )


async def validation_error_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    logger.debug("Handling invalid request for %s %s", request.method, request.url.path)
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder(
            error_response(
                "validation_error",
                "Request validation failed.",
                exc.errors(),
            )
        ),
    )


async def http_error_handler(
    request: Request,
    exc: StarletteHTTPException,
) -> JSONResponse:
    logger.debug("Handling HTTP error for %s %s", request.method, request.url.path)
    detail: Any = exc.detail
    message = detail if isinstance(detail, str) else "The request could not be completed."
    details = None if isinstance(detail, str) else detail
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            error_response(f"http_{exc.status_code}", message, details)
        ),
        headers=exc.headers,
    )


async def database_error_handler(
    request: Request,
    exc: SQLAlchemyError,
) -> JSONResponse:
    logger.exception(
        "Database operation failed for %s %s (%s)",
        request.method,
        request.url.path,
        type(exc).__name__,
    )
    return JSONResponse(
        status_code=500,
        content=error_response("database_error", "A database error occurred."),
    )


async def unexpected_error_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    logger.exception(
        "Unhandled error for %s %s (%s)",
        request.method,
        request.url.path,
        type(exc).__name__,
    )
    return JSONResponse(
        status_code=500,
        content=error_response("internal_error", "An unexpected error occurred."),
    )