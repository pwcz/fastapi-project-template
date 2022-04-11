from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_handle_alive():
    response = client.get("/alive")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
