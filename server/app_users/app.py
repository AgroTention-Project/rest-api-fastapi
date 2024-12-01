from fastapi import APIRouter
from .models import User
from ..lib_auth import Credential
from ..lib_utils.response import Response

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
def get_user_detail(credential: Credential) -> Response[User]:
    pass


@router.delete("/me")
def delete_user(credential: Credential) -> Response[None]:
    pass
