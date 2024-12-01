from fastapi import APIRouter
from . import utils
from .models import News
from ..lib_utils.response import Response
from typing import List

# -------------------------------------------------------------- #
# ---       News
# -------------------------------------------------------------- #
router = APIRouter(prefix="/news", tags=["News"])


@router.get("")
async def get_recent_news(start: int = 0) -> Response[List[News]]:
    news = utils.get_recent_news(start)
    return Response(success=True, data=news)
