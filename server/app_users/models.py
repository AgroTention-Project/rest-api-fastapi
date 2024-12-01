from typing import Any, List, Optional

from pydantic import BaseModel


class UserMetadata(BaseModel):
    creation_timestamp: Optional[int] = None
    last_sign_in_timestamp: Optional[int] = None
    last_refresh_timestamp: Optional[int] = None


class User(BaseModel):
    uid: str
    display_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    photo_url: Optional[str] = None
    provider_id: str
    email_verified: bool
    disabled: bool
    tokens_valid_after_timestamp: int
    user_metadata: UserMetadata
