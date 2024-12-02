"""
Diseases App Module
Contains services, handlers, and routers
"""

from fastapi import APIRouter
from firebase_admin.exceptions import NotFoundError

from ..lib_firebase import fb_fstore
from ..lib_utils.response import Response
from .models import Disease

router = APIRouter(prefix="/diseases")
disease_collection = fb_fstore.collection("diseases")


@router.get("/{disease_slug}", tags=["Diseases"])
async def get_disease_detail(disease_slug: str) -> Response[Disease]:
    """
    Get Disease By Slug
    """
    doc_ref = disease_collection.document(disease_slug)
    doc = await doc_ref.get()
    if not doc.exists:
        raise NotFoundError("disease not found")
    disease = doc.to_dict()
    print(disease)
    disease = Disease.model_validate(disease, strict=False)

    return Response(success=True, data=disease)
