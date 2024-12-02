from fastapi import APIRouter, HTTPException, status
from firebase_admin.exceptions import FirebaseError

from ..lib_firebase import fb_fstore
from ..lib_utils.response import Response
from .models import Plant

router = APIRouter(prefix="/plants")
plants_collection = fb_fstore.collection("plants")


@router.get("/{plant_slug}", tags=["Plants"])
async def get_plant_detail(plant_slug: str) -> Response[Plant]:
    try:
        doc_ref = plants_collection.document(plant_slug)
        doc = await doc_ref.get()
        if not doc.exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Response(success=False, message="plant not found").model_dump(),
            )

        plant = doc.to_dict()
        print(plant)
        plant = Plant.model_validate(plant)

        return Response(success=True, data=plant)

    except FirebaseError as exc:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail=Response(success=False, message="plant not found").model_dump(),
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=Response(success=False, message="plant not found").model_dump(),
        ) from exc
