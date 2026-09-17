import pytest

from calculator import CalculationError, evaluate


def test_addition_and_subtraction():
    assert evaluate("2 + 3 - 1") == 4


def test_precedence_and_parentheses():
    assert evaluate("2 + 3 * 4") == 14
    assert evaluate("(2 + 3) * 4") == 20


def test_decimal_division():
    assert evaluate("7.5 / 2.5") == 3.0


def test_modulo_and_exponentiation():
    assert evaluate("10 % 3") == 1
    assert evaluate("2 ** 3") == 8


def test_unary_signs():
    assert evaluate("-2 + +5") == 3


def test_division_by_zero():
    with pytest.raises(CalculationError):
        evaluate("1 / 0")


def test_invalid_expression():
    with pytest.raises(CalculationError):
        evaluate("2 + unknown")
