#!/usr/bin/env python3
''' This script augments the function
with the correct duck-typed annotations'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' This function contains is augmented
    with the correct duck-typed annotations'''
    if lst:
        return lst[0]
    else:
        return None
