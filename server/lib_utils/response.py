from pydantic import BaseModel
from typing import Optional, TypeVar, Generic, Union, List

T = TypeVar("T", bound=Union[BaseModel, List[BaseModel]])


class Response(BaseModel, Generic[T]):
    success: bool
    message: Optional[str] = None
    data: Optional[T] = None
