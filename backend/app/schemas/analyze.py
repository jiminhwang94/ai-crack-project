from pydantic import BaseModel
from typing import Optional

class AnalyzeCreate(BaseModel):
    crack_id: int
    canal_id: int
    crack_type: str
    pixel_area: int
    severity: str
    model_version: Optional[str] = "v1.0"
