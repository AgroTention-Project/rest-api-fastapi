from typing import Optional

from pydantic import BaseModel


class News(BaseModel):
    title: Optional[str] = None
    link: Optional[str] = None
    publisher: Optional[str] = None
    time: Optional[str] = None
