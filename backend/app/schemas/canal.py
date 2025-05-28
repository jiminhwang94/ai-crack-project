from pydantic import BaseModel

class CanalCreate(BaseModel):
    canal_number: str
    description: str
    region: str
    geojson: str
    center_lat: float
    center_lon: float

class Config:
    from_attributes = True  # ✅ 최신 Pydantic v2