#!/usr/bin/env python3
"""
This module contains a function task_wait_random
that creates a asyncio.Task object
using the wait_random coroutine and returns a
asyncio.Task object
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function takes an integer max_delay and returns
    asyncio.Task object
    Args:
        max_delay (int): maximum delay specified
    Return:
        task (asyncio.Task): Wraps wait_random into a Task and
        schedules its execution returning the Task object.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
