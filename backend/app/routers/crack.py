from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from shapely.geometry import Point, shape
import json

from app.database import get_db
from app.models.canal import CanalInfo
from app.models.crack import CrackRaw  # crack_raw 테이블 모델
from pydantic import BaseModel

router = APIRouter()

# Pydantic 모델
class CrackCreate(BaseModel):
    gps_lat: float
    gps_lon: float
    image_url: str
    user_id: int
    device_type: str
    manual_canal_id: int | None = None  # 수동 선택은 선택적

@router.post("/crack")
def register_crack(crack: CrackCreate, db: Session = Depends(get_db)):
    point = Point(crack.gps_lon, crack.gps_lat)
    canals = db.query(CanalInfo).all()

    matched_canal_id = None
    canal_number = None
    auto_matched = False
    matching_distance_m = None

    for canal in canals:
        try:
            geo = json.loads(canal.geojson)
            polygon = shape(geo)

            if polygon.contains(point):
                matched_canal_id = canal.canal_id
                canal_number = canal.canal_number
                auto_matched = True
                matching_distance_m = 0.0
                break

        except Exception as e:
            continue  # 예외 무시

    db_crack = CrackRaw(
        manual_canal_id=crack.manual_canal_id,
        matched_canal_id=matched_canal_id,
        # 현재 
        #canal_number=canal_number,
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