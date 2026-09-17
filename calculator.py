"""Safe arithmetic expression evaluation."""

from __future__ import annotations

import ast


class CalculationError(Exception):
    """Raised when an arithmetic expression cannot be evaluated."""


def evaluate(expression: str) -> int | float:
    """Evaluate a supported arithmetic expression safely.

    Supported operations are addition, subtraction, multiplication, division,
    modulo, exponentiation, unary signs, and parentheses.
    """
    try:
        tree = ast.parse(expression, mode="eval")
    except (SyntaxError, TypeError, ValueError) as error:
        raise CalculationError("invalid expression") from error

    try:
        return _evaluate_node(tree.body)
    except CalculationError:
        raise
    except (ArithmeticError, OverflowError, TypeError, ValueError) as error:
        raise CalculationError("invalid calculation") from error


def _evaluate_node(node: ast.AST) -> int | float:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise CalculationError("unsupported value")
        return node.value

    if isinstance(node, ast.UnaryOp):
        operand = _evaluate_node(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand
        raise CalculationError("unsupported operator")

    if isinstance(node, ast.BinOp):
        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Mod):
            return left % right
        if isinstance(node.op, ast.Pow):
            return left**right
        raise CalculationError("unsupported operator")

    raise CalculationError("unsupported expression")
