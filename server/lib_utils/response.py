"""Standard Response module"""

from typing import Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel

T = TypeVar("T", bound=Union[BaseModel, List[BaseModel]])


class Response(BaseModel, Generic[T]):
    """
    `Response`
    Standard response for this API
    """

    success: bool
    message: Optional[str] = None
    data: Optional[T] = None
