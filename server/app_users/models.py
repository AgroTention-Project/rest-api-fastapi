from pydantic import BaseModel
from typing import Optional, Any


class User(BaseModel):
    uid: str
    display_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    photo_url: Optional[str] = None
    provider_id: Optional[Any] = None
