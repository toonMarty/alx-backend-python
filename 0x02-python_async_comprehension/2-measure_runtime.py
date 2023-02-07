#!/usr/bin/env python3
"""
This module contains a coroutine measure_runtime that will execute
async_comprehension four times in parallel
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function calculates the runtime of
    async_comprehension by running it four times
    in parallel using gather
    Return:
        run_time(float): the runtime of the
            coroutine async_comprehension
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    run_time = time.perf_counter() - start

    return run_time
