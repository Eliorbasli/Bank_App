from fastapi.testclient import TestClient
from app.main import B_app

client = TestClient(B_app)

def test_register_account():
    response = client.post("/api/v1/register", json={"owner_name": "John Doe"})
    assert response.status_code == 200
    assert response.json()["owner_name"] == "John Doe"

def test_get_account():
    response = client.get("/api/v1/account/1")
    assert response.status_code == 200
    assert "owner_name" in response.json()
