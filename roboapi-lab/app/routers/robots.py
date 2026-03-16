from fastapi import APIRouter, HTTPException

from app.models.schemas import CameraFrameResponse, CommandResponse, MoveCommand, Pose, Robot, RobotCreate, RobotStatus
from app.services.robot_service import RobotService
from app.services.store import ROBOTS

router = APIRouter(prefix="/robots", tags=["robots"])


def ensure_robot(robot_id: str) -> None:
    if robot_id not in ROBOTS:
        raise HTTPException(status_code=404, detail="Robot no encontrado")


@router.get("", response_model=list[Robot], summary="Listar robots")
def list_robots() -> list[Robot]:
    return RobotService.list_robots()


@router.post("", response_model=Robot, summary="Registrar robot")
def create_robot(payload: RobotCreate) -> Robot:
    return RobotService.create_robot(payload)


@router.get("/{robot_id}/status", response_model=RobotStatus, summary="Consultar estado del robot")
def robot_status(robot_id: str) -> RobotStatus:
    ensure_robot(robot_id)
    return RobotService.get_status(robot_id)


@router.get("/{robot_id}/pose", response_model=Pose, summary="Consultar pose estimada")
def robot_pose(robot_id: str) -> Pose:
    ensure_robot(robot_id)
    return RobotService.get_pose(robot_id)


@router.post("/{robot_id}/move", response_model=CommandResponse, summary="Mover robot")
def move_robot(robot_id: str, payload: MoveCommand) -> CommandResponse:
    ensure_robot(robot_id)
    return RobotService.move(robot_id, payload)


@router.post("/{robot_id}/stop", response_model=CommandResponse, summary="Detener robot")
def stop_robot(robot_id: str) -> CommandResponse:
    ensure_robot(robot_id)
    return RobotService.stop(robot_id)


@router.get("/{robot_id}/camera", response_model=CameraFrameResponse, summary="Obtener frame de cámara")
def camera_frame(robot_id: str) -> CameraFrameResponse:
    ensure_robot(robot_id)
    return RobotService.get_camera_frame(robot_id)
