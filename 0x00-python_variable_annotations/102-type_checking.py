#!/usr/bin/env python3
'''This script was validated using mypy'''

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''This function was valifated and corrected using mypy
    necessary changes'''
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = ([12, 72, 91],)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
