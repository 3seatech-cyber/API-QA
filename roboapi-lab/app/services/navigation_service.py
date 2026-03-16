from __future__ import annotations

from uuid import uuid4

from app.models.schemas import NavigationGoalRequest, NavigationResponse, Pose
from app.services.store import LOGS, STATUS, now_iso


class NavigationService:
    @staticmethod
    def send_goal(payload: NavigationGoalRequest) -> NavigationResponse:
        STATUS[payload.robot_id].mode = "moving"
        STATUS[payload.robot_id].last_command = f"goal({payload.x}, {payload.y})"
        LOGS[payload.robot_id].append({
            "timestamp": now_iso(),
            "level": "INFO",
            "message": f"Objetivo de navegación recibido en frame={payload.frame}: ({payload.x}, {payload.y})",
        })
        estimate = max(3.0, abs(payload.x) + abs(payload.y))
        return NavigationResponse(
            robot_id=payload.robot_id,
            accepted=True,
            goal=Pose(x=payload.x, y=payload.y, theta=0.0),
            estimated_time_s=estimate,
            path_id=f"path-{uuid4().hex[:8]}",
        )
