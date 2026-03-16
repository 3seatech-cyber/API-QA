from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class Pose(BaseModel):
    x: float
    y: float
    theta: float


class SensorSnapshot(BaseModel):
    battery: float = Field(..., ge=0, le=100)
    imu: Dict[str, float]
    distance_m: float
    temperature_c: float


class RobotBase(BaseModel):
    name: str
    robot_type: Literal["rover", "arm", "drone", "humanoid", "agv"]
    description: Optional[str] = None


class RobotCreate(RobotBase):
    pass


class Robot(RobotBase):
    id: str
    online: bool


class RobotStatus(BaseModel):
    id: str
    online: bool
    mode: Literal["idle", "moving", "stopped", "error"]
    last_command: Optional[str] = None
    sensors: SensorSnapshot


class MoveCommand(BaseModel):
    linear: float = Field(..., description="Velocidad lineal m/s")
    angular: float = Field(..., description="Velocidad angular rad/s")
    duration_s: float = Field(..., gt=0, le=30)


class CommandResponse(BaseModel):
    robot_id: str
    accepted: bool
    action: str
    detail: str


class CameraFrameResponse(BaseModel):
    robot_id: str
    image_url: str
    timestamp: str
    resolution: str


class VisionRequest(BaseModel):
    image_source: str = Field(..., description="URL, nombre de archivo o identificador lógico")
    task: Literal["detect", "classify", "segment"] = "detect"


class Detection(BaseModel):
    label: str
    confidence: float
    bbox: List[int]


class VisionResponse(BaseModel):
    task: str
    model: str
    detections: List[Detection]
    summary: str


class NavigationGoalRequest(BaseModel):
    robot_id: str
    x: float
    y: float
    frame: str = "map"


class NavigationResponse(BaseModel):
    robot_id: str
    accepted: bool
    goal: Pose
    estimated_time_s: float
    path_id: str


class AgentCommandRequest(BaseModel):
    robot_id: str
    prompt: str
    context: Optional[Dict[str, Any]] = None


class AgentPlanStep(BaseModel):
    step: int
    action: str
    params: Dict[str, Any]


class AgentCommandResponse(BaseModel):
    robot_id: str
    interpreted_intent: str
    answer: str
    plan: List[AgentPlanStep]


class LogEvent(BaseModel):
    timestamp: str
    level: Literal["INFO", "WARN", "ERROR"]
    message: str
