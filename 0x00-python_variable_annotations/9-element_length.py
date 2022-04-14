#!/usr/bin/env python3
''' This script annotates function parameters
and return values with the appropriate types'''

from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' function parameters and return values annotated
    with the appropriate types
    '''
    return [(i, len(i)) for i in lst]
