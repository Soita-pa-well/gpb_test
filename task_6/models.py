import pydantic
from datetime import datetime


class Columns(pydantic.BaseModel):
    key1: int
    key2: datetime
    key3: str
