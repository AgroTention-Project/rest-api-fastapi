from fastapi import APIRouter
from pydantic import BaseModel

from ..lib_utils.response import Response


# -------------------------------------------------------------- #
# ---       Models
# -------------------------------------------------------------- #
class IndexResponse(BaseModel):
    root: str = "see API documentation at /docs"


# -------------------------------------------------------------- #
# ---       Router
# -------------------------------------------------------------- #
router = APIRouter(prefix="", include_in_schema=False)


# -------------------------------------------------------------- #
# ---       Handlers
# -------------------------------------------------------------- #


@router.get(path="/")
def get_index() -> Response[IndexResponse]:
    return Response(success=True, data=IndexResponse())
