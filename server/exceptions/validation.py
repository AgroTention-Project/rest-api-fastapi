"""Module Pydantic and Validation Error Handlers"""

from fastapi import HTTPException, Request
from fastapi.logger import logger
from pydantic import ValidationError
from pydantic.errors import PydanticUserError

from ..lib_utils.response import Response

logger.setLevel("ERROR")


def pydantic_user_error(_: Request, exc: PydanticUserError):
    """Handle Pydantic User Error"""
    logger.error("PYDANTIC ERROR: %s", str(exc))
    raise HTTPException(
        status_code=400,
        detail=Response(
            success=False,
            message=str(exc),
        ).model_dump(),
    ) from exc


def validation_error(_: Request, exc: ValidationError):
    """Handle `ValidationError` from `pydantic`"""
    logger.error("VALIDATION ERROR: %s", str(exc))
    raise HTTPException(
        status_code=400,
        detail=Response(
            success=False,
            message=str(exc),
        ).model_dump(),
    )
