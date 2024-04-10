from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_checkins():
    # check fake data
    response = client.get("/checkins?user=imsosleepyrn")
    assert response.status_code == 200
    assert response.json() == []

    # check real data
    response = client.get("/checkins?user=ned")
    assert response.status_code == 200
    assert len(response.json()) > 0
