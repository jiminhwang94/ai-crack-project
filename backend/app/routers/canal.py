from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.canal import CanalCreate
from app.database import SessionLocal
from app.models.canal import CanalInfo

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/canal")
def create_canal(canal: CanalCreate, db: Session = Depends(get_db)):
    db_canal = CanalInfo(**canal.dict())
    db.add(db_canal)
    db.commit()
    db.refresh(db_canal)
    return db_canal
