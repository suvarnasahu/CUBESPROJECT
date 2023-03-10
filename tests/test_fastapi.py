from fastapi.testclient import TestClient
from wufooform import app

client = TestClient(app)

def test_read_main():
    response = client.get("/forms")
    assert response.status_code == 200
