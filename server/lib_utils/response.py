from pydantic import BaseModel
from typing import Optional, TypeVar, Generic

T = TypeVar("T", bound=BaseModel)


class Response(BaseModel, Generic[T]):
    success: bool
    message: Optional[str] = None
    data: Optional[T] = None
