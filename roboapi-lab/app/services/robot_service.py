from __future__ import annotations

from datetime import datetime, UTC
from uuid import uuid4

from app.models.schemas import CameraFrameResponse, CommandResponse, MoveCommand, Pose, Robot, RobotCreate, RobotStatus
from app.services.store import LOGS, ROBOTS, STATUS


class RobotService:
    @staticmethod
    def list_robots() -> list[Robot]:
        return list(ROBOTS.values())

    @staticmethod
    def create_robot(payload: RobotCreate) -> Robot:
        robot_id = f"{payload.robot_type}-{uuid4().hex[:6]}"
        robot = Robot(id=robot_id, online=True, **payload.model_dump())
        ROBOTS[robot_id] = robot
        STATUS[robot_id] = RobotStatus(
            id=robot_id,
            online=True,
            mode="idle",
            last_command="registered",
            sensors=STATUS["rover-001"].sensors,
        )
        LOGS[robot_id] = [{
            "timestamp": datetime.now(UTC).isoformat(),
            "level": "INFO",
            "message": f"Robot {robot.name} registrado en la plataforma.",
        }]
        return robot

    @staticmethod
    def get_status(robot_id: str) -> RobotStatus:
        return STATUS[robot_id]

    @staticmethod
    def get_pose(robot_id: str) -> Pose:
        seed = sum(ord(c) for c in robot_id) % 10
        return Pose(x=1.0 + seed / 10, y=2.0 + seed / 20, theta=0.15 * seed)

    @staticmethod
    def move(robot_id: str, cmd: MoveCommand) -> CommandResponse:
        status = STATUS[robot_id]
        status.mode = "moving"
        status.last_command = f"move({cmd.linear}, {cmd.angular}, {cmd.duration_s})"
        LOGS[robot_id].append({
            "timestamp": datetime.now(UTC).isoformat(),
            "level": "INFO",
            "message": f"Movimiento aceptado: linear={cmd.linear}, angular={cmd.angular}, duration={cmd.duration_s}s",
        })
        return CommandResponse(
            robot_id=robot_id,
            accepted=True,
            action="move",
            detail="Comando de movimiento aceptado por el controlador del robot.",
        )

    @staticmethod
    def stop(robot_id: str) -> CommandResponse:
        status = STATUS[robot_id]
        status.mode = "stopped"
        status.last_command = "stop"
        LOGS[robot_id].append({
            "timestamp": datetime.now(UTC).isoformat(),
            "level": "WARN",
            "message": "Parada solicitada por la API.",
        })
        return CommandResponse(
            robot_id=robot_id,
            accepted=True,
            action="stop",
            detail="El robot ha detenido su movimiento.",
        )

    @staticmethod
    def get_camera_frame(robot_id: str) -> CameraFrameResponse:
        return CameraFrameResponse(
            robot_id=robot_id,
            image_url=f"https://placehold.co/1280x720?text={robot_id}+camera",
            timestamp=datetime.now(UTC).isoformat(),
            resolution="1280x720",
        )
