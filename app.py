"""Flask API for safe arithmetic calculation.

The POST /api/calculate endpoint accepts JSON of the form
{"expression": "2 + 3"} and returns HTTP 200 with {"result": 5} for
supported expressions.

Invalid requests and expressions return HTTP 400 with a stable JSON error
object. Missing or non-string expressions return {"error": "invalid request"},
malformed or unsupported expressions return {"error": "invalid expression"},
and division by zero returns {"error": "division by zero"}.
"""

from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

from calculator import CalculationError, evaluate


app = Flask(__name__)


@app.post("/api/calculate")
def calculate():
    """Evaluate an arithmetic expression from a JSON request."""
    if not request.is_json:
        return jsonify({"error": "invalid request"}), 400

    try:
        payload = request.get_json()
    except BadRequest:
        return jsonify({"error": "invalid expression"}), 400

    if not isinstance(payload, dict) or not isinstance(
        payload.get("expression"), str
    ):
        return jsonify({"error": "invalid request"}), 400

    try:
        result = evaluate(payload["expression"])
    except CalculationError as error:
        if isinstance(error.__cause__, ZeroDivisionError):
            return jsonify({"error": "division by zero"}), 400
        return jsonify({"error": "invalid expression"}), 400

    return jsonify({"result": result}), 200

