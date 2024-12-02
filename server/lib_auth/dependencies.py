"""
# Module `dependencies`

Contains auth bearer 
"""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from ..lib_firebase import fb_auth
from ..lib_utils.logger import logger
from ..lib_utils.response import Response
from .models import Claims

Credential = Annotated[
    HTTPAuthorizationCredentials,
    Depends(
        HTTPBearer(
            description="JWT token for authentication. example 'Bearer ey102r0v0...'",
            auto_error=False,
        )
    ),
]


def verify_token(credential: Credential) -> Claims:
    """
    ## `verify_token`
    Verify token and return active user claims.
    """

    if credential is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=Response(
                success=False,
                message="unauthorized",
            ).model_dump(),
        )

    token = credential.credentials

    decoded_token = fb_auth.verify_id_token(token, check_revoked=True)
    claims = Claims.model_validate(decoded_token, strict=False)

    logger.info("user log: %s | %s", claims.uid, claims.email)
    return claims


__all__ = ["verify_token", "Credential"]
