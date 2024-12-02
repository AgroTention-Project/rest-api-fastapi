"""Google Api Exception Handler Module"""

from fastapi import HTTPException, Request
from fastapi.logger import logger
from google.api_core.exceptions import GoogleAPICallError

from ..lib_utils.response import Response


def google_cloud_error(_: Request, exc: GoogleAPICallError):
    """Handle exceptions based on `GoogleAPICallError`"""
    logger.error("GOOGLE CLOUD ERROR: %s", str(exc))

    status_code = exc.code if exc.code is not None else 500
    raise HTTPException(
        status_code=status_code,
        detail=Response(success=False, message=f"{str(exc)}").model_dump(),
    ) from exc
