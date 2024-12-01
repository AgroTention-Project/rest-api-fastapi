from fastapi import Depends
from typing import Annotated
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

Credential = Annotated[
    HTTPAuthorizationCredentials,
    Depends(
        HTTPBearer(
            auto_error=True,
            description="JWT token for authentication. example 'Bearer ey102r0v0...'",
        )
    ),
]
