#!/usr/bin/env python3
"""
This script contains an async routine called wait_n
that takes in 2 int arguments (in this order): n and max_delay.
It spawn wait_random n times with the specified max_delay.

wait_n returns the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
"""


import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ wait_n returns the list of all the delays (float values) """
    delays: List[float] = []
    for i in range(n):
        flag = 0
        delay = await wait_random(max_delay)
        if len(delays) == 0:
            delays.append(delay)
            continue

        for j in range(len(delays)):
            if delay < delays[j]:
                delays.insert(j, delay)
                flag = 1
                break

        if flag == 0:
            delays.append(delay)

    return delays
