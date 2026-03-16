# RoboAPI Lab

Laboratorio de APIs con IA para Robótica basado en **FastAPI + Swagger/OpenAPI**. Este repositorio sirve como MVP académico e institucional para conectar robots, sensores, visión artificial y agentes inteligentes mediante servicios web documentados y probables.

## Qué incluye

- API backend con FastAPI y documentación Swagger automática
- Endpoints para:
  - salud del sistema
  - registro y consulta de robots
  - telemetría y estado
  - movimiento y parada
  - captura de cámara simulada
  - visión artificial simulada
  - navegación por objetivos
  - agente IA para interpretar comandos
  - trazabilidad de eventos
- Arquitectura modular para conectar ROS 2, MQTT o hardware real después
- Dockerfile y docker-compose
- Tests básicos con pytest
- Workflow de GitHub Actions
- Propuesta ejecutiva y arquitectura técnica en `docs/`

## Stack

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- Docker / Docker Compose

## Ejecución local

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

La API quedará disponible en:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

## Ejecución con Docker

```bash
docker compose up --build
```

## Estructura

```text
roboapi-lab/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   └── models/
├── docs/
│   ├── propuesta_ejecutiva.md
│   └── arquitectura.md
├── tests/
├── frontend/
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Endpoints principales

- `GET /health`
- `GET /robots`
- `POST /robots`
- `GET /robots/{robot_id}/status`
- `GET /robots/{robot_id}/pose`
- `POST /robots/{robot_id}/move`
- `POST /robots/{robot_id}/stop`
- `GET /robots/{robot_id}/camera`
- `POST /vision/detect`
- `POST /navigation/goal`
- `POST /agent/command`
- `GET /logs/{robot_id}`

## Roadmap sugerido

1. Conectar `RobotService` con ROS 2 topics/services.
2. Sustituir la visión simulada por YOLO o RT-DETR.
3. Sustituir `AgentService` por un LLM local vía Ollama o vLLM.
4. Añadir autenticación JWT, colas Redis y PostgreSQL.
5. Añadir dashboard React en `frontend/`.

## Enfoque académico

Este MVP es útil para cursos y proyectos de:

- robótica móvil
- visión computacional
- integración ROS 2 + web APIs
- agentes inteligentes
- digital twin
- ciberseguridad aplicada a robots conectados


## GitHub Pages para el MVP

Este repositorio incluye una página estática lista para GitHub Pages en la carpeta `docs/`.

### Publicación
1. Sube el repositorio a GitHub.
2. Ve a **Settings > Pages**.
3. Selecciona la rama principal y la carpeta **/docs**.
4. Publica la página.

### Uso con el backend
- Ejecuta o despliega el backend FastAPI.
- Configura en la página la URL base del backend, por ejemplo `http://127.0.0.1:8000` o tu dominio en Render/Railway.
- Abre Swagger desde el botón integrado.
