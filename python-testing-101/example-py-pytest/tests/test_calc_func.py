"""
test_calc_func.py contains pytest tests for math functions.
pytest discovers tests named "test_*".
Each function in this module is a test case.
"""

import pytest
from com.automationpanda.example.calc_func import *

NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_add():
    value = add(NUMBER_1, NUMBER_2)
    assert value == 5.0


def test_subtract():
    value = subtract(NUMBER_1, NUMBER_2)
    assert value == 1.0


def test_subtract_negative():
    value = subtract(NUMBER_2, NUMBER_1)
    assert value == -1.0


def test_multiply():
    value = multiply(NUMBER_1, NUMBER_2)
    assert value == 6.0


def test_divide():
    value = divide(NUMBER_1, NUMBER_2)
    assert value == 1.5


# Test for dividing by zero catches the exception
# http://doc.pytest.org/en/latest/assert.html#assertions-about-expected-exceptions

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        divide(NUMBER_1, 0)
    assert "division by zero" in str(e.value)


# Tests for maximum and minimum use parameters
# http://doc.pytest.org/en/latest/parametrize.html

@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_1),
    (NUMBER_2, NUMBER_1, NUMBER_1),
    (NUMBER_1, NUMBER_1, NUMBER_1),
])
def test_maximum(a, b, expected):
    assert maximum(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_2),
    (NUMBER_2, NUMBER_1, NUMBER_2),
    (NUMBER_2, NUMBER_2, NUMBER_2),
])
def test_minimum(a, b, expected):
    assert minimum(a, b) == expected

# Testes para função logaritmo()
def test_logarithm_base_10():
    assert logarithm(100, 10) == 2.0


def test_logarithm_base_e():
    assert logarithm(math.e, math.e) == 1.0


def test_logarithm_invalid_base():
    with pytest.raises(ValueError):
        logarithm(100, 1)

    with pytest.raises(ValueError):
        logarithm(100, -2)

    with pytest.raises(ValueError):
        logarithm(-5, 10)

# Novos testes para corrigir mutações
def test_log_default_base():
    assert logarithm(100) == math.log(100, 10)

def test_log_zero_value():
    with pytest.raises(ValueError, match="só é definido para números positivos"):
        logarithm(0)

def test_log_value_one_valid():
    assert logarithm(1) == 0  # log base 10 de 1 é 0

def test_log_base_two_valid():
    result = logarithm(8, 2)
    assert result == 3

def test_log_base_one_invalid():
    with pytest.raises(ValueError, match="base do logaritmo.*maior que 1"):
        logarithm(10, 1)
