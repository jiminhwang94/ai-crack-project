from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

# 사용자 정보 테이블
class UserInfo(Base):
    __tablename__ = "user_info"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True)
    affiliation = Column(String(150))  # 소속 또는 회사명
    role = Column(String(50), default="worker")  # worker / admin 구분
    created_at = Column(DateTime, default=datetime.utcnow)
