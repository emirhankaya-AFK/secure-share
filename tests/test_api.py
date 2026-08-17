from fastapi.testclient import TestClient

from app.main import create_app


def test_share_link_can_be_resolved() -> None:
    with TestClient(create_app()) as client:
        created = client.post("/api/v1/shares", json={"filename": "report.pdf", "ttl_seconds": 60})
        token = created.json()["token"]
        resolved = client.get(f"/api/v1/shares/{token}")
    assert created.status_code == 200
    assert resolved.json()["filename"] == "report.pdf"


def test_share_ttl_is_validated() -> None:
    with TestClient(create_app()) as client:
        response = client.post("/api/v1/shares", json={"filename": "x", "ttl_seconds": 5})
    assert response.status_code == 422
