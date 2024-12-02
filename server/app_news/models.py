from typing import Optional

from pydantic import BaseModel


class News(BaseModel):
    title: str
    link: str
    publisher: Optional[str] = None
    time: Optional[str] = None
