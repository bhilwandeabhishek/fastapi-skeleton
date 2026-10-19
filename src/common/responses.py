from typing import Any

from pydantic import BaseModel


class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Any | None = None


class ErrorResponse(BaseModel):
    error: ErrorDetail


ERROR_RESPONSES = {
    404: {
        "model": ErrorResponse,
        "description": "The requested user does not exist.",
    },
    409: {
        "model": ErrorResponse,
        "description": "The user conflicts with an existing record.",
    },
    422: {
        "model": ErrorResponse,
        "description": "The request contains invalid data.",
    },
    500: {
        "model": ErrorResponse,
        "description": "The request could not be completed because of a server error.",
    },
}


def error_response(
    code: str,
    message: str,
    details: Any | None = None,
) -> dict[str, dict[str, Any]]:
    return {
        "error": {
            "code": code,
            "message": message,
            "details": details,
        }
    }