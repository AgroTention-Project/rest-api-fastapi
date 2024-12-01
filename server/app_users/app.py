from fastapi import APIRouter, Depends, status
from .models import User
from fastapi import HTTPException
from ..lib_auth.dependencies import verify_token
from ..lib_auth.models import Claims
from ..lib_utils.response import Response
from ..lib_firebase import fb_auth
from typing import Annotated


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me")
def get_user_detail(
    active_user: Annotated[Claims, Depends(verify_token)]
) -> Response[User]:
    try:
        user_id = active_user.uid
        user = fb_auth.get_user(user_id)
        user = User.model_validate(user, from_attributes=True)
        content = Response(success=True, data=user)
        return content

    except:
        # TODO Better error handling
        return None


@router.delete("/me")
def delete_user(active_user: Annotated[Claims, Depends(verify_token)]) -> Response:
    try:
        user_id = active_user.uid
        fb_auth.delete_user(user_id)
        return Response(success=True, message="delete user succes")
    except:
        pass
