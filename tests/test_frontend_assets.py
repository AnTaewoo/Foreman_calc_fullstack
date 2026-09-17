from pathlib import Path


FRONTEND = Path(__file__).parents[1] / "frontend"


def test_index_loads_react():
    content = (FRONTEND / "index.html").read_text()
    assert "React" in content
    assert "ReactDOM" in content


def test_calculator_controls_exist():
    content = (FRONTEND / "index.html").read_text()
    assert "Clear" in content
    assert "Calculate" in content


def test_expression_operations_exist():
    content = (FRONTEND / "index.html").read_text()
    for operation in ["+", "-", "*", "/", "%", "**"]:
        assert operation in content


def test_frontend_mounts_react_app():
    content = (FRONTEND / "app.js").read_text()
    assert "createRoot" in content or "ReactDOM.render" in content
