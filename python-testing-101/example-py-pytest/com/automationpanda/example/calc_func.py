"""
calc_func.py contains math functions with no side effects.
"""
import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # automatically raises ZeroDivisionError
    return a * 1.0 / b


def maximum(a, b):
    return a if a >= b else b


def minimum(a, b):
    return a if a <= b else b


def logarithm(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)