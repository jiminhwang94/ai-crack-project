# app/routers/match.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shapely.geometry import Point, shape
from app.database import get_db
from app.models.canal import CanalInfo
import json


router = APIRouter()

# 예시 농수로 polygon (경도, 위도 순서) → 실제 DB에서 가져올 예정
canals = [
    {
        "canal_id": 1,
        "name": "농수로 A",
        "polygon": [
            (127.0351, 37.4962),
            (127.0355, 37.4963),
            (127.0356, 37.4960),
            (127.0352, 37.4959)
        ]
    },
    {
        "canal_id": 2,
        "name": "농수로 B",
        "polygon": [
            (127.0345, 37.4950),
            (127.0349, 37.4952),
            (127.0350, 37.4948),
            (127.0346, 37.4946)
        ]
    }
]

@router.post("/match_canal/")
def match_canal(latitude: float, longitude: float, db: Session = Depends(get_db)):
    point = Point(longitude, latitude)
    canals = db.query(CanalInfo).all()

    for canal in canals:
        try:
            geojson_obj = json.loads(canal.geojson)
            polygon = shape(geojson_obj)  # shapely의 shape 함수로 GeoJSON을 Polygon으로 변환

            if polygon.contains(point):
                return {
                    "matched": True,
                    "canal_id": canal.canal_id,
                    "canal_number": canal.canal_number,
                    "region": canal.region
                }
        except Exception as e:
            continue  # 잘못된 형식은 무시

    return {
        "matched": False,
        "message": "해당 위치에 일치하는 농수로가 없습니다."
    }
