from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import SessionLocal
from app.models.analyze import CrackAnalyzed
from app.schemas.analyze import AnalyzeCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/analyze")
def create_analysis(data: AnalyzeCreate, db: Session = Depends(get_db)):
    db_analysis = CrackAnalyzed(
        **data.dict(),
        analyzed_at=datetime.utcnow(),
        user_id=1  # 고정 사용자
    )
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis
