from pydantic import BaseModel
from typing import Optional, Any

{
    "iss": "https://securetoken.google.com/agrotention-project-441716",
    "aud": "agrotention-project-441716",
    "auth_time": 1733064110,
    "user_id": "833Ywj6yOBWgAmSljv76h5MxKlx2",
    "sub": "833Ywj6yOBWgAmSljv76h5MxKlx2",
    "iat": 1733064111,
    "exp": 1733067711,
    "email": "test@gmail.com",
    "email_verified": False,
    "firebase": {
        "identities": {"email": ["test@gmail.com"]},
        "sign_in_provider": "password",
    },
    "uid": "833Ywj6yOBWgAmSljv76h5MxKlx2",
}


class Claims(BaseModel):
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
