from typing import Optional
from pydantic import BaseModel


class MessageDto(BaseModel):
    topic: str
    key: Optional[str] = None
    value: Optional[str] = None
    partition: int = -1
