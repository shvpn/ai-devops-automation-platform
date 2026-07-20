from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ask_endpoint_returns_support_answer() -> None:
    response = client.post("/ask", json={"question": "How do I reset VPN password?"})

    assert response.status_code == 200
    assert response.json() == {
        "answer": "Check the account settings or contact IT support."
    }
