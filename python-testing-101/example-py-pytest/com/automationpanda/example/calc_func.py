"""
calc_func.py contains math functions with no side effects.
"""


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

def sign(a):
    if a > 0:
        return "positive"
    elif a == 0:
        return "zero"
    else:
        return "negative"
