from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LogCreate(BaseModel):
    user_id: int
    action: str
    target_table: str
    target_id: int
    description: Optional[str] = ""

class LogOut(LogCreate):
    log_id: int
    timestamp: datetime

    class Config:
        orm_mode = True
