from pathlib import Path


FRONTEND_APP = Path(__file__).parents[1] / "frontend" / "app.js"


def test_frontend_posts_expression_to_api():
    content = FRONTEND_APP.read_text()
    assert "/api/calculate" in content
    assert "POST" in content
    assert "expression" in content


def test_frontend_renders_result_and_error():
    content = FRONTEND_APP.read_text()
    assert "result" in content
    assert "error" in content


def test_frontend_has_reset_behavior():
    content = FRONTEND_APP.read_text()
    assert "clear" in content or "reset" in content


def test_frontend_handles_failed_requests():
    content = FRONTEND_APP.read_text()
    assert "catch" in content or "response.ok" in content
