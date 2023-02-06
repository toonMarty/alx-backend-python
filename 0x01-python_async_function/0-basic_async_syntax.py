#!/usr/bin/env python3
"""This module contains a corouting wait_random
that is asynchronous"""
import random
import asyncio
import time


async def wait_random(max_delay: int = 10) -> float:
    """
    This function waits for a random delay
    between 0 and max_delay (included and float value)
    seconds and eventually returns it
    Args:
        max_delay (int): the maximum amount of time
            to wait, defaults to 10
    Return:
         time elapsed(float): delay time
    """
    s = time.perf_counter()
    i = random.randint(0, max_delay)
    await asyncio.sleep(i)
    random.randint(0, max_delay)
    elapsed = time.perf_counter() - s

    return elapsed
