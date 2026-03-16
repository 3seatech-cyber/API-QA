from fastapi import APIRouter, HTTPException

from app.models.schemas import AgentCommandRequest, AgentCommandResponse
from app.services.agent_service import AgentService
from app.services.store import ROBOTS

router = APIRouter(prefix="/agent", tags=["agent"])


@router.post("/command", response_model=AgentCommandResponse, summary="Interpretar comando en lenguaje natural")
def command(payload: AgentCommandRequest) -> AgentCommandResponse:
    if payload.robot_id not in ROBOTS:
        raise HTTPException(status_code=404, detail="Robot no encontrado")
    return AgentService.process(payload)
