# Arquitectura técnica del laboratorio

## Vista general

```text
Usuario / Investigador / Estudiante
                |
        Dashboard / Swagger UI / Postman
                |
             FastAPI
   ------------------------------------------
   |                |              |         |
 Robots API      Vision API   Navigation   Agent API
   |                |              |         |
 ROS 2 / MQTT    YOLO / CV     Planner    LLM / Rules
   |_______________________________________________|
                        |
               Robot físico o simulado
```

## Principios de diseño

- desacoplamiento entre hardware y servicios web
- contratos claros mediante OpenAPI
- trazabilidad de eventos y comandos
- modularidad para escalar hacia ROS 2, nube o edge
- reemplazo progresivo de mocks por servicios reales

## Mapeo de endpoints

### Robots
- `GET /robots`
- `POST /robots`
- `GET /robots/{robot_id}/status`
- `GET /robots/{robot_id}/pose`
- `POST /robots/{robot_id}/move`
- `POST /robots/{robot_id}/stop`
- `GET /robots/{robot_id}/camera`

### Visión
- `POST /vision/detect`

### Navegación
- `POST /navigation/goal`

### Agente IA
- `POST /agent/command`

### Trazabilidad
- `GET /logs/{robot_id}`

## Integración futura con hardware real

### Opción 1: ROS 2
Reemplazar los métodos de `RobotService` por publicadores/suscriptores o servicios ROS 2. Los endpoints se mantienen estables y el laboratorio conserva Swagger como interfaz de validación.

### Opción 2: Edge controller
Conectar Raspberry Pi, Jetson o mini PC a través de MQTT o WebSocket y traducir cada endpoint a comandos de bajo nivel.

### Opción 3: Simulación
Integrar Gazebo, Isaac Sim o Webots y mapear `/navigation/goal`, `/robots/{id}/pose` y `/vision/detect` al entorno de simulación.

## Seguridad recomendada para la siguiente fase

- JWT para autenticación de usuarios y robots
- rate limiting
- separación de redes OT/IT
- almacenamiento de logs en base persistente
- auditoría de comandos críticos

## Observabilidad recomendada

- Prometheus para métricas
- Grafana para dashboards
- Loki o ELK para logs
- OpenTelemetry para trazas distribuidas
