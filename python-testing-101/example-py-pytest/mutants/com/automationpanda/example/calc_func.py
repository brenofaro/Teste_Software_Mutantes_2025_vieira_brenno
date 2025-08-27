"""
calc_func.py contains math functions with no side effects.
"""
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


def x_add__mutmut_orig(a, b):
    return a + b


def x_add__mutmut_1(a, b):
    return a - b

x_add__mutmut_mutants : ClassVar[MutantDict] = {
'x_add__mutmut_1': x_add__mutmut_1
}

def add(*args, **kwargs):
    result = _mutmut_trampoline(x_add__mutmut_orig, x_add__mutmut_mutants, args, kwargs)
    return result 

add.__signature__ = _mutmut_signature(x_add__mutmut_orig)
x_add__mutmut_orig.__name__ = 'x_add'


def x_subtract__mutmut_orig(a, b):
    return a - b


def x_subtract__mutmut_1(a, b):
    return a + b

x_subtract__mutmut_mutants : ClassVar[MutantDict] = {
'x_subtract__mutmut_1': x_subtract__mutmut_1
}

def subtract(*args, **kwargs):
    result = _mutmut_trampoline(x_subtract__mutmut_orig, x_subtract__mutmut_mutants, args, kwargs)
    return result 

subtract.__signature__ = _mutmut_signature(x_subtract__mutmut_orig)
x_subtract__mutmut_orig.__name__ = 'x_subtract'


def x_multiply__mutmut_orig(a, b):
    return a * b


def x_multiply__mutmut_1(a, b):
    return a / b

x_multiply__mutmut_mutants : ClassVar[MutantDict] = {
'x_multiply__mutmut_1': x_multiply__mutmut_1
}

def multiply(*args, **kwargs):
    result = _mutmut_trampoline(x_multiply__mutmut_orig, x_multiply__mutmut_mutants, args, kwargs)
    return result 

multiply.__signature__ = _mutmut_signature(x_multiply__mutmut_orig)
x_multiply__mutmut_orig.__name__ = 'x_multiply'


def x_divide__mutmut_orig(a, b):
    # automatically raises ZeroDivisionError
    return a * 1.0 / b


def x_divide__mutmut_1(a, b):
    # automatically raises ZeroDivisionError
    return a * 1.0 * b


def x_divide__mutmut_2(a, b):
    # automatically raises ZeroDivisionError
    return a / 1.0 / b


def x_divide__mutmut_3(a, b):
    # automatically raises ZeroDivisionError
    return a * 2.0 / b

x_divide__mutmut_mutants : ClassVar[MutantDict] = {
'x_divide__mutmut_1': x_divide__mutmut_1, 
    'x_divide__mutmut_2': x_divide__mutmut_2, 
    'x_divide__mutmut_3': x_divide__mutmut_3
}

def divide(*args, **kwargs):
    result = _mutmut_trampoline(x_divide__mutmut_orig, x_divide__mutmut_mutants, args, kwargs)
    return result 

divide.__signature__ = _mutmut_signature(x_divide__mutmut_orig)
x_divide__mutmut_orig.__name__ = 'x_divide'


def x_maximum__mutmut_orig(a, b):
    return a if a >= b else b


def x_maximum__mutmut_1(a, b):
    return a if a > b else b

x_maximum__mutmut_mutants : ClassVar[MutantDict] = {
'x_maximum__mutmut_1': x_maximum__mutmut_1
}

def maximum(*args, **kwargs):
    result = _mutmut_trampoline(x_maximum__mutmut_orig, x_maximum__mutmut_mutants, args, kwargs)
    return result 

maximum.__signature__ = _mutmut_signature(x_maximum__mutmut_orig)
x_maximum__mutmut_orig.__name__ = 'x_maximum'


def x_minimum__mutmut_orig(a, b):
    return a if a <= b else b


def x_minimum__mutmut_1(a, b):
    return a if a < b else b

x_minimum__mutmut_mutants : ClassVar[MutantDict] = {
'x_minimum__mutmut_1': x_minimum__mutmut_1
}

def minimum(*args, **kwargs):
    result = _mutmut_trampoline(x_minimum__mutmut_orig, x_minimum__mutmut_mutants, args, kwargs)
    return result 

minimum.__signature__ = _mutmut_signature(x_minimum__mutmut_orig)
x_minimum__mutmut_orig.__name__ = 'x_minimum'

def x_sign__mutmut_orig(a):
    if a > 0:
        return "positive"
    elif a == 0:
        return "zero"
    else:
        return "negative"

def x_sign__mutmut_1(a):
    if a >= 0:
        return "positive"
    elif a == 0:
        return "zero"
    else:
        return "negative"

def x_sign__mutmut_2(a):
    if a > 1:
        return "positive"
    elif a == 0:
        return "zero"
    else:
        return "negative"

def x_sign__mutmut_3(a):
    if a > 0:
        return "XXpositiveXX"
    elif a == 0:
        return "zero"
    else:
        return "negative"

def x_sign__mutmut_4(a):
    if a > 0:
        return "POSITIVE"
    elif a == 0:
        return "zero"
    else:
        return "negative"

def x_sign__mutmut_5(a):
    if a > 0:
        return "positive"
    elif a != 0:
        return "zero"
    else:
        return "negative"

def x_sign__mutmut_6(a):
    if a > 0:
        return "positive"
    elif a == 1:
        return "zero"
    else:
        return "negative"

def x_sign__mutmut_7(a):
    if a > 0:
        return "positive"
    elif a == 0:
        return "XXzeroXX"
    else:
        return "negative"

def x_sign__mutmut_8(a):
    if a > 0:
        return "positive"
    elif a == 0:
        return "ZERO"
    else:
        return "negative"

def x_sign__mutmut_9(a):
    if a > 0:
        return "positive"
    elif a == 0:
        return "zero"
    else:
        return "XXnegativeXX"

def x_sign__mutmut_10(a):
    if a > 0:
        return "positive"
    elif a == 0:
        return "zero"
    else:
        return "NEGATIVE"

x_sign__mutmut_mutants : ClassVar[MutantDict] = {
'x_sign__mutmut_1': x_sign__mutmut_1, 
    'x_sign__mutmut_2': x_sign__mutmut_2, 
    'x_sign__mutmut_3': x_sign__mutmut_3, 
    'x_sign__mutmut_4': x_sign__mutmut_4, 
    'x_sign__mutmut_5': x_sign__mutmut_5, 
    'x_sign__mutmut_6': x_sign__mutmut_6, 
    'x_sign__mutmut_7': x_sign__mutmut_7, 
    'x_sign__mutmut_8': x_sign__mutmut_8, 
    'x_sign__mutmut_9': x_sign__mutmut_9, 
    'x_sign__mutmut_10': x_sign__mutmut_10
}

def sign(*args, **kwargs):
    result = _mutmut_trampoline(x_sign__mutmut_orig, x_sign__mutmut_mutants, args, kwargs)
    return result 

sign.__signature__ = _mutmut_signature(x_sign__mutmut_orig)
x_sign__mutmut_orig.__name__ = 'x_sign'

import math

def x_logarithm__mutmut_orig(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_1(a, base=11):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_2(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a < 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_3(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 1:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_4(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError(None)
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_5(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("XXO logaritmo só é definido para números positivos.XX")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_6(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("o logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_7(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O LOGARITMO SÓ É DEFINIDO PARA NÚMEROS POSITIVOS.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_8(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base < 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_9(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 2:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_10(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError(None)
    return math.log(a, base)

def x_logarithm__mutmut_11(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("XXA base do logaritmo deve ser maior que 1.XX")
    return math.log(a, base)

def x_logarithm__mutmut_12(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("a base do logaritmo deve ser maior que 1.")
    return math.log(a, base)

def x_logarithm__mutmut_13(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A BASE DO LOGARITMO DEVE SER MAIOR QUE 1.")
    return math.log(a, base)

def x_logarithm__mutmut_14(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(None, base)

def x_logarithm__mutmut_15(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, None)

def x_logarithm__mutmut_16(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(base)

def x_logarithm__mutmut_17(a, base=10):
    """
    Retorna o logaritmo de 'a' na base especificada.
    Levanta ValueError se 'a' <= 0 ou base <= 1.
    """
    if a <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 1:
        raise ValueError("A base do logaritmo deve ser maior que 1.")
    return math.log(a, )

x_logarithm__mutmut_mutants : ClassVar[MutantDict] = {
'x_logarithm__mutmut_1': x_logarithm__mutmut_1, 
    'x_logarithm__mutmut_2': x_logarithm__mutmut_2, 
    'x_logarithm__mutmut_3': x_logarithm__mutmut_3, 
    'x_logarithm__mutmut_4': x_logarithm__mutmut_4, 
    'x_logarithm__mutmut_5': x_logarithm__mutmut_5, 
    'x_logarithm__mutmut_6': x_logarithm__mutmut_6, 
    'x_logarithm__mutmut_7': x_logarithm__mutmut_7, 
    'x_logarithm__mutmut_8': x_logarithm__mutmut_8, 
    'x_logarithm__mutmut_9': x_logarithm__mutmut_9, 
    'x_logarithm__mutmut_10': x_logarithm__mutmut_10, 
    'x_logarithm__mutmut_11': x_logarithm__mutmut_11, 
    'x_logarithm__mutmut_12': x_logarithm__mutmut_12, 
    'x_logarithm__mutmut_13': x_logarithm__mutmut_13, 
    'x_logarithm__mutmut_14': x_logarithm__mutmut_14, 
    'x_logarithm__mutmut_15': x_logarithm__mutmut_15, 
    'x_logarithm__mutmut_16': x_logarithm__mutmut_16, 
    'x_logarithm__mutmut_17': x_logarithm__mutmut_17
}

def logarithm(*args, **kwargs):
    result = _mutmut_trampoline(x_logarithm__mutmut_orig, x_logarithm__mutmut_mutants, args, kwargs)
    return result 

logarithm.__signature__ = _mutmut_signature(x_logarithm__mutmut_orig)
x_logarithm__mutmut_orig.__name__ = 'x_logarithm'
