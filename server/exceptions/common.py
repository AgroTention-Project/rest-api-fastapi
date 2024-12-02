from fastapi import HTTPException, Request
from fastapi.logger import logger

from ..lib_utils.response import Response

logger.setLevel("ERROR")


def common_error(req: Request, exc: Exception):
    logger.error(f"UNHANDELED ERROR {str(exc)}")
    raise HTTPException(
        status_code=500,
        detail=Response(
            success=False,
            message=f"{str(exc)}",
        ).model_dump(),
    ) from exc
