"""
News App Module
"""

from typing import List

from fastapi import APIRouter

from ..lib_utils.logger import logger
from ..lib_utils.response import Response
from . import utils
from .models import News

router = APIRouter(prefix="/news", tags=["News"])


@router.get("")
async def get_recent_news() -> Response[List[News]]:
    """
    Handler for Get List of Recent News
    """
    news = []
    for i in range(0, 101, 10):
        logger.info("scrapping news page %d", i / 10)
        news += utils.get_recent_news(i)
    return Response(success=True, data=news)
