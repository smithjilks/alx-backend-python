#!/usr/bin/env python3
"""This script imports async_comprehension from the previous file
and contains a measure_runtime coroutine
that will execute async_comprehension four times
in parallel using asyncio.gather."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measures the total runtime and returns it."""
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    return end_time - start_time
