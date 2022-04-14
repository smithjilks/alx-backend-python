#!/usr/bin/env python3
''' This script contains a type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float. '''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''sum_list is a type-annotated function sum_list
    which takes a list input_list of floats as argument
    and returns their sum as a float.
    '''
    res = 0
    for i in input_list:
        res = res + i
    return res
