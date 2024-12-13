"""
Models for scan results
"""

import datetime
from typing import Optional

from pydantic import BaseModel


class Result(BaseModel):
    """
    scan result model
    """

    user_id: str
    plant_slug: str
    is_healthy: bool
    disease_slug: Optional[str] = None
    scanned_at: Optional[int] = int(datetime.datetime.now().timestamp())
