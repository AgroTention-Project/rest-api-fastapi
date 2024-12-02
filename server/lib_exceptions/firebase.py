"""Firebase Exceptions Handler"""

from fastapi import HTTPException, Request
# Codes
from firebase_admin.exceptions import (ABORTED, ALREADY_EXISTS, CANCELLED,
                                       CONFLICT, DATA_LOSS, DEADLINE_EXCEEDED,
                                       FAILED_PRECONDITION, INTERNAL,
                                       INVALID_ARGUMENT, NOT_FOUND,
                                       OUT_OF_RANGE, PERMISSION_DENIED,
                                       RESOURCE_EXHAUSTED, UNAUTHENTICATED,
                                       UNAVAILABLE, UNKNOWN, FirebaseError)

from ..lib_utils.logger import logger
from ..lib_utils.response import Response


def firebase_error(_: Request, exc: FirebaseError):
    """Firebase Error Handler handle every exception based on `FirebaseError`"""
    logger.error("FIREBASE ERROR: %s", str(exc))
    if exc.code in [NOT_FOUND]:
        status_code = 404
    elif exc.code in [CONFLICT, ALREADY_EXISTS, ABORTED]:
        status_code = 409
    elif exc.code in [INVALID_ARGUMENT, FAILED_PRECONDITION, OUT_OF_RANGE]:
        status_code = 400
    elif exc.code in [UNAUTHENTICATED]:
        status_code = 401
    elif exc.code in [PERMISSION_DENIED]:
        status_code = 403
    elif exc.code in [RESOURCE_EXHAUSTED]:
        status_code = 429
    elif exc.code in [CANCELLED, DEADLINE_EXCEEDED]:
        status_code = 408
    elif exc.code in [UNKNOWN, INTERNAL, DATA_LOSS]:
        status_code = 500
    elif exc.code in [UNAVAILABLE]:
        status_code = 503
    else:
        status_code = 500  # Default status code untuk error yang tidak dikenal

    raise HTTPException(
        status_code=status_code,
        detail=Response(success=False, message=f"{exc}").model_dump(),
    ) from exc
