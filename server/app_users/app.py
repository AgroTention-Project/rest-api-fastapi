"""
App Users Module
"""

from io import BytesIO
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from PIL import Image

from ..lib_auth.dependencies import verify_token
from ..lib_auth.models import Claims
from ..lib_firebase import fb_auth, fb_fstore, fb_storage
from ..lib_utils.response import Response
from .models import UpdateUserExtras, User, UserExtras

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)
users_extras_coll = fb_fstore.collection("users_extras")


@router.get("/me", tags=["GET"])
def get_user_detail(
    active_user: Annotated[Claims, Depends(verify_token)]
) -> Response[User]:
    """Get Firebase User Detail (Same as firebase.auth.getUser)"""
    user_id = active_user.uid
    user = fb_auth.get_user(user_id)
    user = User.model_validate(user, from_attributes=True)
    return Response(success=True, data=user)


@router.delete("/me", tags=["DELETE"])
async def delete_user(
    active_user: Annotated[Claims, Depends(verify_token)]
) -> Response:
    """Delete user and extras information (if exist)"""
    user_id = active_user.uid
    fb_auth.delete_user(user_id)
    doc_ref = users_extras_coll.document(user_id)
    extras = await doc_ref.get()
    if extras.exists:
        await doc_ref.delete()
    return Response(success=True, message=f"delete user {user_id} succes")


@router.get("/me/extras", tags=["GET"])
async def get_or_create_user_extras(
    active_user: Annotated[Claims, Depends(verify_token)]
) -> Response[UserExtras]:
    """Get user extras data or create default value if not exist"""
    user_id = active_user.uid
    doc_ref = users_extras_coll.document(user_id)
    doc = await doc_ref.get()
    if not doc.exists:
        new_data = UserExtras(
            is_admin=False,
            is_expert=False,
            company=None,
            role_at_company=None,
        ).model_dump()
        await doc_ref.create(new_data)

    doc = await doc_ref.get()
    data = UserExtras.model_validate(doc.to_dict())
    return Response(success=True, data=data)


@router.patch("/me/extras", tags=["PATCH"])
async def update_user_extras(
    body: UpdateUserExtras,
    active_user: Annotated[Claims, Depends(verify_token)],
):
    """Update user extras information"""
    user_id = active_user.uid
    doc_ref = users_extras_coll.document(user_id)
    await doc_ref.update(body.model_dump())
    return Response(success=True, message=f"success update user {user_id}")


@router.post("/me/profile-photo", tags=["POST"])
async def update_or_create_photo_profile(
    image: UploadFile,
    active_user: Annotated[Claims, Depends(verify_token)],
):
    """Create or update (if exist) user photo profile and
    add `photo_url` data into user information"""
    if not image.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail=Response(
                success=False, message="invalid image file format"
            ).model_dump(),
        )
    contents = await image.read()
    img = Image.open(BytesIO(contents))
    img_buffer = BytesIO()
    img.save(img_buffer, format="JPEG")
    img_buffer.seek(0)
    storage_path = f"profile-photos/{active_user.uid}.jpg"
    blob = fb_storage.blob(storage_path)
    blob.upload_from_string(img_buffer.getvalue(), content_type="image/jpeg")
    blob.make_public()
    public_url = blob.public_url
    fb_auth.update_user(uid=active_user.uid, photo_url=public_url)
    return Response(success=True)
