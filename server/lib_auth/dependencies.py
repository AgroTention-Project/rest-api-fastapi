"""
# Module `dependencies`

Contains auth bearer 
"""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.logger import logger
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin.exceptions import FirebaseError

from ..lib_firebase import fb_auth
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

    Parameters:
        `credential (Credential)`: Request `Authorization` header (ex: `Bearer ey29vj13...`)


    Returns:
        `Claims`

    Raises:
        `HTTPException`
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

    try:
        decoded_token = fb_auth.verify_id_token(token, check_revoked=True)
        claims = Claims.model_validate(decoded_token, strict=False)
        logger.info(f"user log: {claims.uid} | {claims.email}")
        return claims

    except ValueError as exc:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=Response(
                success=False,
                message="invalid id token",
            ).model_dump(),
        ) from exc

    except FirebaseError as exc:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=Response(
                success=False,
                message=f"{exc.code}: {str(exc)}",
            ).model_dump(),
        ) from exc

    except Exception as exc:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=Response(
                success=False,
                message="unhandeled client error",
            ).model_dump(),
        ) from exc


__all__ = ["verify_token", "Credential"]
