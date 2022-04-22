#!/usr/bin/env python3
"""This script contains a function async_generator that takes no arguments."""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ a coroutine called async_generator that takes no arguments."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
