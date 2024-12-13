"""
module scanner services
"""

from PIL import Image
from uuid import uuid4
from ..lib_firebase import fb_fstore

results_collection = fb_fstore.collection("results")


async def create_scan_result(user_id: str, data: dict):
    """Create Scan Result

    Save scan result
    """
    doc_ref = results_collection.document(str(uuid4()))
    await doc_ref.create(data)


async def get_scan_result(user_id: str, result_id: str):
    """Get Scan Result by id

    Get result by id
    """


async def delete_scan_reult(user_id: str, result_id: str):
    """Delete Scan Result by id

    Delete result by id
    """


async def list_scan_result(user_id: str):
    """List Scan Result by id

    Get result by id
    """
