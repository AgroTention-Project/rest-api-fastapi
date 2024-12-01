from typing import Optional

from pydantic import BaseModel, Field


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


class UserExtras(BaseModel):
    is_admin: bool = Field(default=False)
    is_expert: bool = Field(default=False)
    company: Optional[str] = Field(default=None)
    role_at_company: Optional[str] = Field(default=None)


user = UserExtras()
