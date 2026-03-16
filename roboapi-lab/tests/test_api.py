from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_list_robots() -> None:
    response = client.get("/robots")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_agent_command() -> None:
    response = client.post(
        "/agent/command",
        json={"robot_id": "rover-001", "prompt": "Inspecciona la mesa y dime si hay piezas rojas"},
    )
    assert response.status_code == 200
    assert response.json()["interpreted_intent"] == "inspection_task"
