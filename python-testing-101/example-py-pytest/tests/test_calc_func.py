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

# --- NOVOS TESTES ---
def test_divide_identity():
    """Dividir por 1 deve retornar o próprio número."""
    assert divide(5, 1) == 5.0

def test_divide_fraction():
    """Testa frações que revelam diferença entre a*1.0/b e a/1.0/b."""
    assert divide(2, 2) == 1.0
    assert divide(5, 2) == 2.5


# --- Maximum / Minimum edge cases ---
def test_maximum_equal_numbers():
    """Máximo de dois números iguais deve ser o próprio número."""
    assert maximum(7, 7) == 7

def test_minimum_equal_numbers():
    """Mínimo de dois números iguais deve ser o próprio número."""
    assert minimum(7, 7) == 7
