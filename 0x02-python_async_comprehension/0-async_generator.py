#!/usr/bin/env python3
"""
This module contains a coroutine,
async_generator that loops 10 times
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine takes no arguments and loops 10 times,
    each time asynchronously waiting for 1 second and
    yielding a random number between 0 and 10
    Return:
        Generator[float, None, None]
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
