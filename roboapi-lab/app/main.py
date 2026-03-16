from fastapi import FastAPI

from app.routers.agent import router as agent_router
from app.routers.health import router as health_router
from app.routers.logs import router as logs_router
from app.routers.navigation import router as navigation_router
from app.routers.robots import router as robots_router
from app.routers.vision import router as vision_router

app = FastAPI(
    title="RoboAPI Lab",
    version="0.1.0",
    description=(
        "Laboratorio de APIs con IA para Robótica. "
        "MVP académico para exponer capacidades de robots, visión y agentes mediante Swagger/OpenAPI."
    ),
    contact={
        "name": "RoboAPI Lab Team",
        "email": "lab@example.com",
    },
)

app.include_router(health_router)
app.include_router(robots_router)
app.include_router(vision_router)
app.include_router(navigation_router)
app.include_router(agent_router)
app.include_router(logs_router)
