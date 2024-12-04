"""
Models for scan results
"""

import datetime
from typing import Optional

from pydantic import BaseModel


class BoxModel(BaseModel):
    """
    Bounding box model
    """

    y_min: int
    y_max: int
    x_min: int
    x_max: int
    label: str


class Result(BaseModel):
    """
    scan result model
    """

    user_id: str
    plant_slug: str
    is_healthy: bool
    disease_slug: Optional[str] = None
    box: BoxModel
    scanned_at: Optional[int] = int(datetime.datetime.now().timestamp())
