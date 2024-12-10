"""
scanner app module
"""

from fastapi import APIRouter
from . import services

router = APIRouter(prefix="/results", tags=["Results"])


@router.post("", tags=["POST"])
async def create_scan_result(data: dict):
    """Create Scan Result

    Save scan result from prediction
    """
    user_id = ""
    await services.create_scan_result(user_id, data)


@router.get("", tags=["GET"])
async def list_scan_result(result_id: str):
    """List Scan Result by id

    Get result by id
    """

    user_id = ""
    await services.list_scan_result(user_id=user_id)


@router.get("/{result_id}", tags=["GET"])
async def get_scan_result(result_id: str):
    """Get Scan Result by id

    Get result by id
    """
    user_id = ""
    await services.get_scan_result(user_id, result_id)


@router.delete("/{result_id}", tags=["DELETE"])
async def delete_scan_result(result_id: str):
    """Delete Scan Result by id

    Delete result by id
    """
    user_id = ""
    await services.delete_scan_reult(user_id, result_id)
