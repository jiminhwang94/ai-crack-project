from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class LogHistory(Base):
    __tablename__ = "log_history"

    log_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)                         # 작업자 ID
    action = Column(String(50))                       # 작업 유형 (등록, 수정 등)
    target_table = Column(String(100))                # 대상 테이블 (예: canal_info)
    target_id = Column(Integer)                       # 대상 행의 ID
    description = Column(String(255))                 # 설명 (예: “농수로 C-001 등록”)
    timestamp = Column(DateTime, default=datetime.utcnow)
