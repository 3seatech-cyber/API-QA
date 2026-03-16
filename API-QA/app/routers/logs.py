from fastapi import APIRouter, HTTPException

from app.models.schemas import LogEvent
from app.services.store import LOGS

router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("/{robot_id}", response_model=list[LogEvent], summary="Consultar trazabilidad del robot")
def get_logs(robot_id: str) -> list[LogEvent]:
    if robot_id not in LOGS:
        raise HTTPException(status_code=404, detail="No existen logs para ese robot")
    return [LogEvent(**item) for item in LOGS[robot_id]]
