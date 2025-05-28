from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

# 균열 촬영 정보 테이블
class CrackRaw(Base):
    __tablename__ = "crack_raw"

    crack_id = Column(Integer, primary_key=True, index=True)
    manual_canal_id = Column(Integer)         # 사용자가 선택한 canal
    matched_canal_id = Column(Integer)        # 자동 매칭된 canal (나중에 매칭)
    image_url = Column(String)
    gps_lat = Column(Float)
    gps_lon = Column(Float)
    captured_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, default=1)      # 현재는 고정값 1
    device_type = Column(String, default="Mobile")
    matching_distance_m = Column(Float, default=0.0)
    auto_matched = Column(Integer, default=0)  # 0: false, 1: true
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
