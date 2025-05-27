from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from app.database import Base
from datetime import datetime

class CanalInfo(Base):
    __tablename__ = "canal_info"

    canal_id = Column(Integer, primary_key=True, index=True)
    canal_number = Column(String(50), unique=True)
    description = Column(Text)
    region = Column(String(100))
    geojson = Column(Text)
    center_lat = Column(Float)
    center_lon = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
