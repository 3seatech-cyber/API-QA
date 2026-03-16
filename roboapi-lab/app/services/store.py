from __future__ import annotations

from datetime import datetime, UTC
from typing import Dict, List

from app.models.schemas import Robot, RobotStatus, SensorSnapshot


def now_iso() -> str:
    return datetime.now(UTC).isoformat()


ROBOTS: Dict[str, Robot] = {
    "rover-001": Robot(
        id="rover-001",
        name="Rover Explorer",
        robot_type="rover",
        description="Rover académico para navegación indoor.",
        online=True,
    )
}

STATUS: Dict[str, RobotStatus] = {
    "rover-001": RobotStatus(
        id="rover-001",
        online=True,
        mode="idle",
        last_command="boot",
        sensors=SensorSnapshot(
            battery=88.5,
            imu={"ax": 0.01, "ay": -0.02, "gz": 0.005},
            distance_m=1.75,
            temperature_c=32.1,
        ),
    )
}

LOGS: Dict[str, List[dict]] = {
    "rover-001": [
        {"timestamp": now_iso(), "level": "INFO", "message": "Robot iniciado correctamente."},
        {"timestamp": now_iso(), "level": "INFO", "message": "Esperando comandos."},
    ]
}
