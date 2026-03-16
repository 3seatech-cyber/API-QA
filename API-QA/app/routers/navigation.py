from fastapi import APIRouter, HTTPException

from app.models.schemas import NavigationGoalRequest, NavigationResponse
from app.services.navigation_service import NavigationService
from app.services.store import ROBOTS

router = APIRouter(prefix="/navigation", tags=["navigation"])


@router.post("/goal", response_model=NavigationResponse, summary="Enviar objetivo de navegación")
def send_goal(payload: NavigationGoalRequest) -> NavigationResponse:
    if payload.robot_id not in ROBOTS:
        raise HTTPException(status_code=404, detail="Robot no encontrado")
    return NavigationService.send_goal(payload)
