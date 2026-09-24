from fastapi.testclient import TestClient
from app.main import app

def test_health_echo_and_metrics():
    c=TestClient(app)
    assert c.get("/health").json()["status"]=="ok"
    assert c.post("/echo",json={"text":"hello"}).json()["echo"]=="hello"
    assert c.post("/echo",json={"text":""}).status_code==422
    metrics=c.get("/metrics")
    assert metrics.status_code==200
    assert "demo_http_requests_total" in metrics.text
    assert 'path="/echo"' in metrics.text
