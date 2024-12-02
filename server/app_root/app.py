"""Index App"""

from fastapi import APIRouter
from pydantic import BaseModel

from ..lib_utils.response import Response


class IndexResponse(BaseModel):
    """Index Response Model"""

    root: str = "see API documentation at /docs"


router = APIRouter(prefix="", include_in_schema=False)


@router.get(path="/")
def get_index() -> Response[IndexResponse]:
    """Index Handler"""
    return Response(success=True, data=IndexResponse())
