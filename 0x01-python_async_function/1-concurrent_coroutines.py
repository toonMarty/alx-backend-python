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
    create_wait_random = []

    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(lambda y: elapsed_time.append(y.result()))
        create_wait_random.append(task)

    for element in create_wait_random:
        await element

    return elapsed_time
