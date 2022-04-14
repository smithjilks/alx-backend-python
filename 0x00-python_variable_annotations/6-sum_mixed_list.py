#!/usr/bin/env python3
''' This script contains a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float. '''


from typing import Union, List

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' sum_mixed_list a type-annotated function sum_mixed_list
    which takes a list mxd_lst of integers and floats
    and returns their sum as a float.
    '''
    sum = 0
    for i in mxd_lst:
        sum = sum + float(i)
    return sum
