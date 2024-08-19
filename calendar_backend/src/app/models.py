from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventModel(BaseModel):
    title: str
    description: Optional[str]
    start_time: datetime
    end_time: datetime
