# app/routers/match.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shapely.geometry import Point, shape
from app.database import get_db
from app.models.canal import CanalInfo
from shapely.ops import nearest_points
import json

router = APIRouter()

def match_canal(lat: float, lon: float, db, buffer_m: float = 20.0):
    point = Point(lon, lat)
    canals = db.query(CanalInfo).all()

    closest_canal = None
    min_distance = float("inf")

    for canal in canals:
        try:
            geojson_obj = json.loads(canal.geojson)
            polygon = shape(geojson_obj)
            
            print(f"[CHECK] Testing canal {canal.canal_id}")  # ✅ loop 확인용

            # ① PIP 검사
            if polygon.contains(point):
                print(f"[PIP MATCH] canal_id={canal.canal_id}")
                return {
                    "matched": True,
                    "canal_id": canal.canal_id,
                    "canal_number": canal.canal_number,
                    "region": canal.region,
                    "distance_m": 0.0
                }

            # ② Buffer 검사 (20m 이내 허용)
            buffer_degree = buffer_m / 111320  # 위도 경도 1도 ≈ 111,320m
            buffered = polygon.buffer(buffer_degree)

            if buffered.contains(point):
                print(f"[BUFFER CONTAINS] point matched canal_id={canal.canal_id}")
                nearest_point = nearest_points(polygon, point)[0]
                distance = point.distance(nearest_point) * 111320  # 도 → m
                
                print(f"[DISTANCE] canal_id={canal.canal_id} → distance = {distance} m")

                if distance < min_distance:
                    min_distance = distance
                    closest_canal = canal

        except Exception as e:
            continue

    # ③ 가장 가까운 농수로가 있으면 반환
    if closest_canal:
        print(f"[PRINT] canal_id={closest_canal.canal_id}, dist={min_distance}")
        
        return {
            "matched": True,
            "canal_id": closest_canal.canal_id,
            "canal_number": closest_canal.canal_number,
            "region": closest_canal.region,
            "distance_m": round(min_distance, 2)
        }

    # ④ 실패
    return {
        "matched": False,
        "message": "일치 또는 인근 농수로 없음"
    }
       
# 수동 테스트용 라우터
@router.post("/match_canal/")
def match_canal_api(latitude: float, longitude: float, db: Session = Depends(get_db)):
    return match_canal(latitude, longitude, db)

