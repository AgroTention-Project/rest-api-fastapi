"""Module Token Claims Model"""

from typing import Any, Optional

from pydantic import BaseModel


class Claims(BaseModel):
    """Token Claims Model"""

    iss: Optional[str] = None
    aud: Optional[str] = None
    auth_time: Optional[int] = None
    user_id: Optional[str] = None
    sub: Optional[str] = None
    iat: Optional[int] = None
    exp: Optional[int] = None
    email: Optional[str] = None
    email_verified: Optional[bool] = None
    uid: Optional[str] = None
    fireabase: Any = None
