"""
scanner app module
"""

from fastapi import APIRouter, UploadFile
from ..lib_utils.tensorflow import (
    predict_rice_image,
    predict_potato_image,
    predict_tomato_image,
)
from . import services
import io

router = APIRouter(prefix="/scanner", tags=["Results"])


@router.post("/", tags=["Scanner"])
async def scan_plant(file: UploadFile, plant: str):
    """Plant Scanner"""

    contents = await file.read()
    image_io = io.BytesIO(contents)

    match plant:
        case "rice":
            result = predict_rice_image(image_io)
            return result

        case "potato":
            result = predict_potato_image(image_io)

        case "tomato":
            result = predict_tomato_image(image_io)

    return result


@router.post("/results", tags=["POST"])
async def create_scan_result(data: dict):
    """Create Scan Result

    Save scan result from prediction
    """
    user_id = ""
    await services.create_scan_result(user_id, data)


@router.get("/results", tags=["GET"])
async def list_scan_result(result_id: str):
    """List Scan Result by id

    Get result by id
    """

    user_id = ""
    await services.list_scan_result(user_id=user_id)


@router.get("/results/{result_id}", tags=["GET"])
async def get_scan_result(result_id: str):
    """Get Scan Result by id

    Get result by id
    """
    user_id = ""
    await services.get_scan_result(user_id, result_id)


@router.delete("/results/{result_id}", tags=["DELETE"])
async def delete_scan_result(result_id: str):
    """Delete Scan Result by id

    Delete result by id
    """
    user_id = ""
    await services.delete_scan_reult(user_id, result_id)
