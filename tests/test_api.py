from app import app


def test_calculate_success():
    with app.test_client() as client:
        response = client.post(
            "/api/calculate",
            json={"expression": "2 + 3 * 4"},
        )

    assert response.status_code == 200
    assert response.get_json() == {"result": 14}


def test_calculate_decimal():
    with app.test_client() as client:
        response = client.post(
            "/api/calculate",
            json={"expression": "7.5 / 2.5"},
        )

    assert response.status_code == 200
    assert response.get_json() == {"result": 3.0}


def test_missing_expression():
    with app.test_client() as client:
        response = client.post("/api/calculate", json={})

    assert response.status_code == 400
    assert response.get_json() == {"error": "invalid request"}


def test_invalid_expression():
    with app.test_client() as client:
        response = client.post(
            "/api/calculate",
            json={"expression": "2 + unknown"},
        )

    assert response.status_code == 400
    assert response.get_json() == {"error": "invalid expression"}


def test_division_by_zero():
    with app.test_client() as client:
        response = client.post(
            "/api/calculate",
            json={"expression": "1 / 0"},
        )

    assert response.status_code == 400
    assert response.get_json() == {"error": "division by zero"}

