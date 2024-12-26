from pydantic import BaseModel
from datetime import datetime


class Token(BaseModel):
    username: str
    exp_date: datetime
