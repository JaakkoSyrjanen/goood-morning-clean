from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RoomRequest(BaseModel):
    room_number: str

@router.post("/checkin/room")
def check_room(data: RoomRequest):
    # This is where PMS lookup logic would go
    return {
        "room": data.room_number,
        "entitlement": {
            "breakfast_included": True,
            "num_people": 2
        },
        "message": "Room check simulated"
    }
