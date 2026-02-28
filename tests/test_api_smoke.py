from fastapi.testclient import TestClient

from src.api import app


def test_health():
    c = TestClient(app)
    r = c.get('/health')
    assert r.status_code == 200


def test_generate_validation():
    c = TestClient(app)
    r = c.post('/generate', json={'topic': '   '})
    assert r.status_code == 422
