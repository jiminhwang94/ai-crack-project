# app/routers/crack.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.models.crack import CrackRaw
from app.routers.match import match_canal  # 자동 매칭 함수 임포트
from pydantic import BaseModel

router = APIRouter()

class CrackCreate(BaseModel):
    gps_lat: float
    gps_lon: float
    image_url: str
    user_id: int
    device_type: str
    manual_canal_id: int | None = None

@router.post("/crack")
def register_crack(crack: CrackCreate, db: Session = Depends(get_db)):
    # 자동 매칭 로직
    match_result = match_canal(crack.gps_lat, crack.gps_lon, db)

    matched_canal_id = None
    canal_number = None
    auto_matched = False
    matching_distance_m = None

    if match_result.get("matched"):
        matched_canal_id = match_result["canal_id"]
        canal_number = match_result["canal_number"]
        auto_matched = True
        matching_distance_m = match_result.get("distance_m", 0.0)
    else:
        auto_matched = False

    db_crack = CrackRaw(
        manual_canal_id=crack.manual_canal_id,
        matched_canal_id=matched_canal_id,
        canal_number=canal_number,
        image_url=crack.image_url,
        gps_lat=crack.gps_lat,
        gps_lon=crack.gps_lon,
        captured_at=datetime.utcnow(),
        user_id=crack.user_id,
        device_type=crack.device_type,
        auto_matched=auto_matched,
        matching_distance_m=matching_distance_m,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    db.add(db_crack)
    db.commit()
    db.refresh(db_crack)

    return {
        "message": "Crack registered successfully.",
        "crack_id": db_crack.crack_id,
        "matched": auto_matched,
        "matched_canal_id": matched_canal_id,
        "canal_number": canal_number
    }
