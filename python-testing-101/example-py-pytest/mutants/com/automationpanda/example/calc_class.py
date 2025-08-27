"""
calc_class.py contains the Calculator class.
It uses the math functions from calc_func.
"""

from com.automationpanda.example.calc_func import *
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


class Calculator(object):
    def xǁCalculatorǁ__init____mutmut_orig(self):
        self._last_answer = 0.0
    def xǁCalculatorǁ__init____mutmut_1(self):
        self._last_answer = None
    def xǁCalculatorǁ__init____mutmut_2(self):
        self._last_answer = 1.0
    
    xǁCalculatorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁ__init____mutmut_1': xǁCalculatorǁ__init____mutmut_1, 
        'xǁCalculatorǁ__init____mutmut_2': xǁCalculatorǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCalculatorǁ__init____mutmut_orig)
    xǁCalculatorǁ__init____mutmut_orig.__name__ = 'xǁCalculatorǁ__init__'

    @property
    def last_answer(self):
        return self._last_answer

    def xǁCalculatorǁ_do_math__mutmut_orig(self, a, b, func):
        self._last_answer = func(a, b)
        return self.last_answer

    def xǁCalculatorǁ_do_math__mutmut_1(self, a, b, func):
        self._last_answer = None
        return self.last_answer

    def xǁCalculatorǁ_do_math__mutmut_2(self, a, b, func):
        self._last_answer = func(None, b)
        return self.last_answer

    def xǁCalculatorǁ_do_math__mutmut_3(self, a, b, func):
        self._last_answer = func(a, None)
        return self.last_answer

    def xǁCalculatorǁ_do_math__mutmut_4(self, a, b, func):
        self._last_answer = func(b)
        return self.last_answer

    def xǁCalculatorǁ_do_math__mutmut_5(self, a, b, func):
        self._last_answer = func(a, )
        return self.last_answer
    
    xǁCalculatorǁ_do_math__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁ_do_math__mutmut_1': xǁCalculatorǁ_do_math__mutmut_1, 
        'xǁCalculatorǁ_do_math__mutmut_2': xǁCalculatorǁ_do_math__mutmut_2, 
        'xǁCalculatorǁ_do_math__mutmut_3': xǁCalculatorǁ_do_math__mutmut_3, 
        'xǁCalculatorǁ_do_math__mutmut_4': xǁCalculatorǁ_do_math__mutmut_4, 
        'xǁCalculatorǁ_do_math__mutmut_5': xǁCalculatorǁ_do_math__mutmut_5
    }
    
    def _do_math(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁ_do_math__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁ_do_math__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _do_math.__signature__ = _mutmut_signature(xǁCalculatorǁ_do_math__mutmut_orig)
    xǁCalculatorǁ_do_math__mutmut_orig.__name__ = 'xǁCalculatorǁ_do_math'

    def xǁCalculatorǁadd__mutmut_orig(self, a, b):
        return self._do_math(a, b, add)

    def xǁCalculatorǁadd__mutmut_1(self, a, b):
        return self._do_math(None, b, add)

    def xǁCalculatorǁadd__mutmut_2(self, a, b):
        return self._do_math(a, None, add)

    def xǁCalculatorǁadd__mutmut_3(self, a, b):
        return self._do_math(a, b, None)

    def xǁCalculatorǁadd__mutmut_4(self, a, b):
        return self._do_math(b, add)

    def xǁCalculatorǁadd__mutmut_5(self, a, b):
        return self._do_math(a, add)

    def xǁCalculatorǁadd__mutmut_6(self, a, b):
        return self._do_math(a, b, )
    
    xǁCalculatorǁadd__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁadd__mutmut_1': xǁCalculatorǁadd__mutmut_1, 
        'xǁCalculatorǁadd__mutmut_2': xǁCalculatorǁadd__mutmut_2, 
        'xǁCalculatorǁadd__mutmut_3': xǁCalculatorǁadd__mutmut_3, 
        'xǁCalculatorǁadd__mutmut_4': xǁCalculatorǁadd__mutmut_4, 
        'xǁCalculatorǁadd__mutmut_5': xǁCalculatorǁadd__mutmut_5, 
        'xǁCalculatorǁadd__mutmut_6': xǁCalculatorǁadd__mutmut_6
    }
    
    def add(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁadd__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁadd__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add.__signature__ = _mutmut_signature(xǁCalculatorǁadd__mutmut_orig)
    xǁCalculatorǁadd__mutmut_orig.__name__ = 'xǁCalculatorǁadd'

    def xǁCalculatorǁsubtract__mutmut_orig(self, a, b):
        return self._do_math(a, b, subtract)

    def xǁCalculatorǁsubtract__mutmut_1(self, a, b):
        return self._do_math(None, b, subtract)

    def xǁCalculatorǁsubtract__mutmut_2(self, a, b):
        return self._do_math(a, None, subtract)

    def xǁCalculatorǁsubtract__mutmut_3(self, a, b):
        return self._do_math(a, b, None)

    def xǁCalculatorǁsubtract__mutmut_4(self, a, b):
        return self._do_math(b, subtract)

    def xǁCalculatorǁsubtract__mutmut_5(self, a, b):
        return self._do_math(a, subtract)

    def xǁCalculatorǁsubtract__mutmut_6(self, a, b):
        return self._do_math(a, b, )
    
    xǁCalculatorǁsubtract__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁsubtract__mutmut_1': xǁCalculatorǁsubtract__mutmut_1, 
        'xǁCalculatorǁsubtract__mutmut_2': xǁCalculatorǁsubtract__mutmut_2, 
        'xǁCalculatorǁsubtract__mutmut_3': xǁCalculatorǁsubtract__mutmut_3, 
        'xǁCalculatorǁsubtract__mutmut_4': xǁCalculatorǁsubtract__mutmut_4, 
        'xǁCalculatorǁsubtract__mutmut_5': xǁCalculatorǁsubtract__mutmut_5, 
        'xǁCalculatorǁsubtract__mutmut_6': xǁCalculatorǁsubtract__mutmut_6
    }
    
    def subtract(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁsubtract__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁsubtract__mutmut_mutants"), args, kwargs, self)
        return result 
    
    subtract.__signature__ = _mutmut_signature(xǁCalculatorǁsubtract__mutmut_orig)
    xǁCalculatorǁsubtract__mutmut_orig.__name__ = 'xǁCalculatorǁsubtract'

    def xǁCalculatorǁmultiply__mutmut_orig(self, a, b):
        return self._do_math(a, b, multiply)

    def xǁCalculatorǁmultiply__mutmut_1(self, a, b):
        return self._do_math(None, b, multiply)

    def xǁCalculatorǁmultiply__mutmut_2(self, a, b):
        return self._do_math(a, None, multiply)

    def xǁCalculatorǁmultiply__mutmut_3(self, a, b):
        return self._do_math(a, b, None)

    def xǁCalculatorǁmultiply__mutmut_4(self, a, b):
        return self._do_math(b, multiply)

    def xǁCalculatorǁmultiply__mutmut_5(self, a, b):
        return self._do_math(a, multiply)

    def xǁCalculatorǁmultiply__mutmut_6(self, a, b):
        return self._do_math(a, b, )
    
    xǁCalculatorǁmultiply__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁmultiply__mutmut_1': xǁCalculatorǁmultiply__mutmut_1, 
        'xǁCalculatorǁmultiply__mutmut_2': xǁCalculatorǁmultiply__mutmut_2, 
        'xǁCalculatorǁmultiply__mutmut_3': xǁCalculatorǁmultiply__mutmut_3, 
        'xǁCalculatorǁmultiply__mutmut_4': xǁCalculatorǁmultiply__mutmut_4, 
        'xǁCalculatorǁmultiply__mutmut_5': xǁCalculatorǁmultiply__mutmut_5, 
        'xǁCalculatorǁmultiply__mutmut_6': xǁCalculatorǁmultiply__mutmut_6
    }
    
    def multiply(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁmultiply__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁmultiply__mutmut_mutants"), args, kwargs, self)
        return result 
    
    multiply.__signature__ = _mutmut_signature(xǁCalculatorǁmultiply__mutmut_orig)
    xǁCalculatorǁmultiply__mutmut_orig.__name__ = 'xǁCalculatorǁmultiply'

    def xǁCalculatorǁdivide__mutmut_orig(self, a, b):
        return self._do_math(a, b, divide)

    def xǁCalculatorǁdivide__mutmut_1(self, a, b):
        return self._do_math(None, b, divide)

    def xǁCalculatorǁdivide__mutmut_2(self, a, b):
        return self._do_math(a, None, divide)

    def xǁCalculatorǁdivide__mutmut_3(self, a, b):
        return self._do_math(a, b, None)

    def xǁCalculatorǁdivide__mutmut_4(self, a, b):
        return self._do_math(b, divide)

    def xǁCalculatorǁdivide__mutmut_5(self, a, b):
        return self._do_math(a, divide)

    def xǁCalculatorǁdivide__mutmut_6(self, a, b):
        return self._do_math(a, b, )
    
    xǁCalculatorǁdivide__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁdivide__mutmut_1': xǁCalculatorǁdivide__mutmut_1, 
        'xǁCalculatorǁdivide__mutmut_2': xǁCalculatorǁdivide__mutmut_2, 
        'xǁCalculatorǁdivide__mutmut_3': xǁCalculatorǁdivide__mutmut_3, 
        'xǁCalculatorǁdivide__mutmut_4': xǁCalculatorǁdivide__mutmut_4, 
        'xǁCalculatorǁdivide__mutmut_5': xǁCalculatorǁdivide__mutmut_5, 
        'xǁCalculatorǁdivide__mutmut_6': xǁCalculatorǁdivide__mutmut_6
    }
    
    def divide(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁdivide__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁdivide__mutmut_mutants"), args, kwargs, self)
        return result 
    
    divide.__signature__ = _mutmut_signature(xǁCalculatorǁdivide__mutmut_orig)
    xǁCalculatorǁdivide__mutmut_orig.__name__ = 'xǁCalculatorǁdivide'

    def xǁCalculatorǁmaximum__mutmut_orig(self, a, b):
        return self._do_math(a, b, maximum)

    def xǁCalculatorǁmaximum__mutmut_1(self, a, b):
        return self._do_math(None, b, maximum)

    def xǁCalculatorǁmaximum__mutmut_2(self, a, b):
        return self._do_math(a, None, maximum)

    def xǁCalculatorǁmaximum__mutmut_3(self, a, b):
        return self._do_math(a, b, None)

    def xǁCalculatorǁmaximum__mutmut_4(self, a, b):
        return self._do_math(b, maximum)

    def xǁCalculatorǁmaximum__mutmut_5(self, a, b):
        return self._do_math(a, maximum)

    def xǁCalculatorǁmaximum__mutmut_6(self, a, b):
        return self._do_math(a, b, )
    
    xǁCalculatorǁmaximum__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁmaximum__mutmut_1': xǁCalculatorǁmaximum__mutmut_1, 
        'xǁCalculatorǁmaximum__mutmut_2': xǁCalculatorǁmaximum__mutmut_2, 
        'xǁCalculatorǁmaximum__mutmut_3': xǁCalculatorǁmaximum__mutmut_3, 
        'xǁCalculatorǁmaximum__mutmut_4': xǁCalculatorǁmaximum__mutmut_4, 
        'xǁCalculatorǁmaximum__mutmut_5': xǁCalculatorǁmaximum__mutmut_5, 
        'xǁCalculatorǁmaximum__mutmut_6': xǁCalculatorǁmaximum__mutmut_6
    }
    
    def maximum(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁmaximum__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁmaximum__mutmut_mutants"), args, kwargs, self)
        return result 
    
    maximum.__signature__ = _mutmut_signature(xǁCalculatorǁmaximum__mutmut_orig)
    xǁCalculatorǁmaximum__mutmut_orig.__name__ = 'xǁCalculatorǁmaximum'

    def xǁCalculatorǁminimum__mutmut_orig(self, a, b):
        return self._do_math(a, b, minimum)

    def xǁCalculatorǁminimum__mutmut_1(self, a, b):
        return self._do_math(None, b, minimum)

    def xǁCalculatorǁminimum__mutmut_2(self, a, b):
        return self._do_math(a, None, minimum)

    def xǁCalculatorǁminimum__mutmut_3(self, a, b):
        return self._do_math(a, b, None)

    def xǁCalculatorǁminimum__mutmut_4(self, a, b):
        return self._do_math(b, minimum)

    def xǁCalculatorǁminimum__mutmut_5(self, a, b):
        return self._do_math(a, minimum)

    def xǁCalculatorǁminimum__mutmut_6(self, a, b):
        return self._do_math(a, b, )
    
    xǁCalculatorǁminimum__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁminimum__mutmut_1': xǁCalculatorǁminimum__mutmut_1, 
        'xǁCalculatorǁminimum__mutmut_2': xǁCalculatorǁminimum__mutmut_2, 
        'xǁCalculatorǁminimum__mutmut_3': xǁCalculatorǁminimum__mutmut_3, 
        'xǁCalculatorǁminimum__mutmut_4': xǁCalculatorǁminimum__mutmut_4, 
        'xǁCalculatorǁminimum__mutmut_5': xǁCalculatorǁminimum__mutmut_5, 
        'xǁCalculatorǁminimum__mutmut_6': xǁCalculatorǁminimum__mutmut_6
    }
    
    def minimum(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁminimum__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁminimum__mutmut_mutants"), args, kwargs, self)
        return result 
    
    minimum.__signature__ = _mutmut_signature(xǁCalculatorǁminimum__mutmut_orig)
    xǁCalculatorǁminimum__mutmut_orig.__name__ = 'xǁCalculatorǁminimum'
