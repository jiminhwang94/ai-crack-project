import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# .env에서 연결 문자열 가져오기
SQLALCHEMY_DATABASE_URL = os.getenv("AZURE_SQL_URL")

# 데이터베이스 엔진 생성 (Azure SQL + pyodbc)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
)

# 세션 클래스 정의
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 (모든 모델이 이걸 상속받음)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()