from fastapi import HTTPException, Request
from fastapi.logger import logger
from pydantic.errors import PydanticUserError

from ..lib_utils.response import Response

logger.setLevel("ERROR")


def pydantic_user_error(req: Request, exc: PydanticUserError):
    logger.error(f"PYDANTIC ERROR {str(exc)}")
    raise HTTPException(
        status_code=400,
        detail=Response(
            success=False,
            message=str(exc),
        ).model_dump(),
    ) from exc
