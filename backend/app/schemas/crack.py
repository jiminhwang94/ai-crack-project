from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CrackCreate(BaseModel):
    manual_canal_id: int | None = None
    matched_canal_id: Optional[int] = None
    image_url: str
    gps_lat: float
    gps_lon: float
    canal_number: Optional[str] = None
    device_type: Optional[str] = "Mobile"
    matching_distance_m: Optional[float] = 0.0
    auto_matched: Optional[int] = 0
