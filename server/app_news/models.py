"""Module News Models"""

from typing import Optional

from pydantic import BaseModel


class News(BaseModel):
    """News Model"""

    title: str
    link: str
    publisher: Optional[str] = None
    time: Optional[str] = None
