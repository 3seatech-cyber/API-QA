from __future__ import annotations

from app.models.schemas import Detection, VisionRequest, VisionResponse


class VisionService:
    @staticmethod
    def infer(payload: VisionRequest) -> VisionResponse:
        detections = [
            Detection(label="person", confidence=0.97, bbox=[32, 48, 220, 420]),
            Detection(label="red_box", confidence=0.91, bbox=[410, 180, 610, 390]),
        ]
        return VisionResponse(
            task=payload.task,
            model="mock-yolo-robotics-v1",
            detections=detections,
            summary=f"Se detectaron {len(detections)} elementos en la fuente {payload.image_source}.",
        )
