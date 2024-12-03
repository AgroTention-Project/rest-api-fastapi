"""Module News Models"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class News(BaseModel):
    """News Model"""

    title: str
    link: str
    publisher: Optional[str] = None
    time: Optional[str] = None
    accessed_by_server_at: Optional[int] = int(datetime.now().timestamp())
