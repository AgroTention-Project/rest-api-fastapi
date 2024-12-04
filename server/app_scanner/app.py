"""
scanner app module
"""

from fastapi import APIRouter, UploadFile, HTTPException


from ..lib_utils.response import Response

router = APIRouter(prefix="/scan", tags=["Scanner"])


@router.post("/{plant_slug}", tags=["POST"])
def scan_plant(plant_slug: str, image: UploadFile):
    """
    Scan plant diseases
    """
    if "image/" not in image.content_type:
        raise HTTPException(
            status_code=400,
            detail=Response(
                success=False,
                message="invalid image type",
            ).model_dump(),
        )

    return plant_slug


@router.get("/results", tags=["Results", "GET"])
def list_scan_results():
    """
    List user scan results
    """


@router.get("/results/{result_id}", tags=["Results", "GET"])
def get_scan_result():
    """
    Get scan result for current user
    """


@router.delete("/results/{result_id}", tags=["Results", "DELETE"])
def delete_scan_result():
    """
    Delete scan result for current user
    """
