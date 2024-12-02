from fastapi import HTTPException, Request
from fastapi.logger import logger
from google.api_core.exceptions import GoogleAPICallError

from ..lib_utils.response import Response

logger.setLevel(level="ERROR")


def google_cloud_error(req: Request, exc: GoogleAPICallError):

    logger.error(f"GOOGLE CLOUD ERROR: {str(exc)}")

    status_code = exc.code if exc.code != None else 500
    raise HTTPException(
        status_code=status_code,
        detail=Response(success=False, message=f"{str(exc)}").model_dump(),
    ) from exc
