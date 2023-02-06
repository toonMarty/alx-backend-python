#!/usr/bin/env python3
"""
This module contains a coroutine wait_n that
returns the list of all the delays
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function wait_n returns the list of all the delays.
    The list of the delays are in ascending order
    without using sort() because of concurrency
    Args:
        n (int): the number of times to spawn wait_random
        max_delay (int): the maximum delay specified
    Return:
        sorted_elapsed_time(list): a sorted list of delays
    """
    elapsed_time = []
    sorted_elapsed_time = []

    for i in range(n):
        task = await asyncio.create_task(wait_random(max_delay))
        elapsed_time.append(task)

    return sorted(elapsed_time)
