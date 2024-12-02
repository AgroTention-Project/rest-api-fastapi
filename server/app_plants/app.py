"""
Plants App Module
"""

from fastapi import APIRouter
from firebase_admin.exceptions import NotFoundError

from ..lib_firebase import fb_fstore
from ..lib_utils.response import Response
from .models import Plant

router = APIRouter(prefix="/plants")
plants_collection = fb_fstore.collection("plants")


@router.get("/{plant_slug}", tags=["Plants"])
async def get_plant_detail(plant_slug: str) -> Response[Plant]:
    """
    Get Plant Information by Plant Slug
    """
    doc_ref = plants_collection.document(plant_slug)
    doc = await doc_ref.get()
    if not doc.exists:
        raise NotFoundError("plant not found")
    plant = doc.to_dict()
    print(plant)
    plant = Plant.model_validate(plant)

    return Response(success=True, data=plant)
