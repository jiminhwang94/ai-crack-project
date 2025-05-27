from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class CrackAnalyzed(Base):
    __tablename__ = "crack_analyzed"

    analyze_id = Column(Integer, primary_key=True, index=True)
    crack_id = Column(Integer)  # crack_raw의 ID (분석 대상)
    canal_id = Column(Integer)  # 연관된 농수로 ID
    crack_type = Column(String)  # 균열 유형 (예: "길이형", "벌어짐", 등)
    pixel_area = Column(Integer)  # 균열 크기 (픽셀 단위)
    severity = Column(String)  # 심각도 등급 (양호/주의/위험/긴급처리)
    analyzed_at = Column(DateTime, default=datetime.utcnow)
    model_version = Column(String, default="v1.0")
    user_id = Column(Integer, default=1)
