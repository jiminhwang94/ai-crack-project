from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.crack import CrackRaw
from app.schemas.crack import CrackCreate
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/crack")
def create_crack(crack: CrackCreate, db: Session = Depends(get_db)):
    db_crack = CrackRaw(
        **crack.dict(),
        user_id=1,  # 고정
        captured_at=datetime.utcnow(),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_crack)
    db.commit()
    db.refresh(db_crack)
    return db_crack
