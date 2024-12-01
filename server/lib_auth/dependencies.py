from ..lib_firebase import fb_auth
from ..lib_utils.response import Response
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.logger import logger
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
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

bearer = HTTPBearer()


def verify_token(credential: Credential) -> Claims:
    if credential == None:
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
        print(decoded_token)
        claims = Claims.model_validate(decoded_token, strict=False)
        return claims

    except Exception as exc:
        logger.error(exc)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=Response(
                success=False,
                message="unauthorized",
            ).model_dump(),
        )
