#!/usr/bin/env python3
''' This script contains a type-annotated function make_multiplier
that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
from typing import Callable
'''


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' make_multiplire is a type-annotated function make_multiplier
    that takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier.
    '''
    def mult(n: float) -> float:
        return multiplier * n
    return mult
