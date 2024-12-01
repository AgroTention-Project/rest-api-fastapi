from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from firebase_admin.exceptions import NOT_FOUND, FirebaseError

from ..lib_auth.dependencies import verify_token
from ..lib_auth.models import Claims
from ..lib_firebase import fb_auth, fb_fstore
from ..lib_utils.response import Response
from .models import User, UserExtras

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)
users_extras_coll = fb_fstore.collection("users_extras")


@router.get("/me")
def get_user_detail(
    active_user: Annotated[Claims, Depends(verify_token)]
) -> Response[User]:
    try:
        user_id = active_user.uid
        user = fb_auth.get_user(user_id)
        user = User.model_validate(user, from_attributes=True)
        return Response(success=True, data=user)

    except FirebaseError as exc:
        code = exc.code

        if code == NOT_FOUND:
            status_code = status.HTTP_404_NOT_FOUND
        else:
            status_code = status.HTTP_424_FAILED_DEPENDENCY
        raise HTTPException(
            status_code=status_code,
            detail=Response(success=False, message=str(exc)).model_dump(),
        ) from exc

    except Exception as exc:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        raise HTTPException(
            status_code=status_code,
            detail=Response(success=False, message=str(exc)).model_dump(),
        ) from exc


@router.delete("/me")
def delete_user(active_user: Annotated[Claims, Depends(verify_token)]) -> Response:
    try:
        user_id = active_user.uid
        fb_auth.delete_user(user_id)
        return Response(success=True, message="delete user succes")

    except FirebaseError as exc:
        code = exc.code

        if code == NOT_FOUND:
            status_code = status.HTTP_404_NOT_FOUND
        else:
            status_code = status.HTTP_424_FAILED_DEPENDENCY
        raise HTTPException(
            status_code=status_code,
            detail=Response(success=False, message=str(exc)).model_dump(),
        ) from exc

    except Exception as exc:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        raise HTTPException(
            status_code=status_code,
            detail=Response(success=False, message=str(exc)).model_dump(),
        ) from exc


@router.get("/me/extras")
async def get_or_create_user_extras(
    active_user: Annotated[Claims, Depends(verify_token)]
) -> Response[UserExtras]:
    try:
        user_id = active_user.uid
        doc_ref = users_extras_coll.document(user_id)
        doc = await doc_ref.get()
        if not doc.exists:
            new_data = UserExtras().model_dump()
            doc_ref.create(new_data)

        doc = await doc_ref.get()
        data = UserExtras.model_validate(doc.to_dict())
        return Response(success=True, data=data)

    except FirebaseError as exc:
        code = exc.code

        if code == NOT_FOUND:
            status_code = status.HTTP_404_NOT_FOUND
        else:
            status_code = status.HTTP_424_FAILED_DEPENDENCY
        raise HTTPException(
            status_code=status_code,
            detail=Response(success=False, message=str(exc)).model_dump(),
        ) from exc

    except Exception as exc:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        raise HTTPException(
            status_code=status_code,
            detail=Response(success=False, message=str(exc)).model_dump(),
        ) from exc
