#!/usr/bin/env python3
"""This module contains a function that
finds the runtime for wait_n
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures the total execution time for
    wait_n and finds the run time of wait n for given
    n and max_delay
    Args:
        n (int): the number of times the coroutine runs
        max_delay (int): maximum delay specified
    Return:
        run_time(float): taverage of total execution time
    """

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start

    run_time = elapsed_time / n
    return run_time
