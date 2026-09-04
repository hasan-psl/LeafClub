def test_health_check_returns_200(client):
    """Test that GET /health returns HTTP 200 and expected status payload."""
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["app"] == "LeafClub"
    assert "environment" in payload


def test_root_endpoint_returns_200(client):
    """Test that GET / returns HTTP 200 and root welcome payload."""
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert "message" in payload
    assert payload["health"] == "/health"
