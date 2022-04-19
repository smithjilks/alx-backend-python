#!/usr/bin/env python3
"""task_wait_random that takes an integer max_delay
and returns a asyncio.Task."""

import asyncio
import random
import time
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ task_wait_random that takes an integer max_delay
    and returns a asyncio.Task."""
    task = asyncio.ensure_future(wait_random(max_delay))
    return task
