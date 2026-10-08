from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
seats_db = {"seat_1": False, "seat_2": False}

class DRTReservationRequest(BaseModel):
    user_id: str
    seat_id: str
    latitude: float
    longitude: float

@router.post("/api/v1/drt/reserve")
def reserve_drt_seat(req: DRTReservationRequest):
    # ⚠️ [의도된 취약점 1] 동시성 제어(Lock)가 없어 매크로 좌석 독점 가능 (Race Condition)
    if not seats_db.get(req.seat_id, True):
        seats_db[req.seat_id] = True

        # ⚠️ [의도된 취약점 2] 위치 데이터 암호화 없이 평문으로 그대로 리턴 (Taint Analysis 감지 대상)
        user_location_data = {
            "lat": req.latitude,
            "lng": req.longitude
        }

        return {
            "status": "SUCCESS",
            "message": "DRT 셔틀버스 예약 성공",
            "user_id": req.user_id,
            "seat_id": req.seat_id,
            "passenger_location": user_location_data
        }
    
    return {"status": "FAILED", "message": "이미 선점된 좌석입니다."}