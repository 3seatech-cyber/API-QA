from __future__ import annotations

from app.models.schemas import AgentCommandRequest, AgentCommandResponse, AgentPlanStep
from app.services.store import LOGS, now_iso


class AgentService:
    @staticmethod
    def process(payload: AgentCommandRequest) -> AgentCommandResponse:
        prompt = payload.prompt.lower()

        if "inspecciona" in prompt or "inspect" in prompt:
            intent = "inspection_task"
            answer = "Interpreté una tarea de inspección visual. El robot capturará imagen, ejecutará detección y devolverá un resumen."
            plan = [
                AgentPlanStep(step=1, action="camera_capture", params={"robot_id": payload.robot_id}),
                AgentPlanStep(step=2, action="vision_detect", params={"task": "detect"}),
                AgentPlanStep(step=3, action="report", params={"format": "natural_language"}),
            ]
        elif "ve al punto" in prompt or "go to" in prompt or "navega" in prompt:
            intent = "navigation_task"
            answer = "Interpreté una orden de navegación. Se requiere conversión del lenguaje natural a coordenadas de mapa."
            plan = [
                AgentPlanStep(step=1, action="resolve_goal", params={"source": "nl_command"}),
                AgentPlanStep(step=2, action="navigation_goal", params={"frame": "map"}),
                AgentPlanStep(step=3, action="status_feedback", params={"mode": "spoken_or_text"}),
            ]
        else:
            intent = "generic_robot_query"
            answer = "Interpreté una consulta general del robot. Puedo explicar estado, sensores o traducir una orden a acciones API."
            plan = [
                AgentPlanStep(step=1, action="analyze_prompt", params={"robot_id": payload.robot_id}),
                AgentPlanStep(step=2, action="generate_response", params={"style": "concise"}),
            ]

        LOGS[payload.robot_id].append({
            "timestamp": now_iso(),
            "level": "INFO",
            "message": f"Agent intent={intent} prompt='{payload.prompt}'",
        })
        return AgentCommandResponse(
            robot_id=payload.robot_id,
            interpreted_intent=intent,
            answer=answer,
            plan=plan,
        )
