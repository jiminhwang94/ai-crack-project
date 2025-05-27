from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.log import LogHistory
from app.schemas.log import LogCreate, LogOut
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/log", response_model=LogOut)
def create_log(log: LogCreate, db: Session = Depends(get_db)):
    db_log = LogHistory(**log.dict(), timestamp=datetime.utcnow())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

@router.get("/log", response_model=list[LogOut])
def list_logs(db: Session = Depends(get_db)):
    return db.query(LogHistory).order_by(LogHistory.timestamp.desc()).all()
