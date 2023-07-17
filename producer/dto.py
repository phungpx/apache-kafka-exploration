from typing import Optional
from pydantic import BaseModel


class MessageDto(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None
    partition: Optional[int] = None
