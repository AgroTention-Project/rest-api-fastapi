from pydantic import BaseModel
from typing import Optional


class News(BaseModel):
    title: Optional[str] = None
    link: Optional[str] = None
    publisher: Optional[str] = None
    time: Optional[str] = None
