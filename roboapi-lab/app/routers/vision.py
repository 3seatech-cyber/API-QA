from fastapi import APIRouter

from app.models.schemas import VisionRequest, VisionResponse
from app.services.vision_service import VisionService

router = APIRouter(prefix="/vision", tags=["vision"])


@router.post("/detect", response_model=VisionResponse, summary="Ejecutar visión artificial")
def detect(payload: VisionRequest) -> VisionResponse:
    return VisionService.infer(payload)
