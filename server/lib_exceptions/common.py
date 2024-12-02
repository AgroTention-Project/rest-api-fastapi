"""Module Common Exceptions Handlers"""

from fastapi import HTTPException, Request

from ..lib_utils.logger import logger
from ..lib_utils.response import Response


def common_error(_: Request, exc: Exception):
    """Common Error Handler handle base `Exception`"""
    logger.error("UNHANDELED ERROR %s", str(exc))
    raise HTTPException(
        status_code=500,
        detail=Response(
            success=False,
            message=f"{str(exc)}",
        ).model_dump(),
    ) from exc
