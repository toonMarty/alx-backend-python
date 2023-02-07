#!/usr/bin/env python3
"""
This module contains a coroutine async_comprehension
that collects 10 random numbers using an async comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function takes no arguments and collects
    10 random numbers from async_generator and
    returns the 10 random numbers
    Return:
         collection(list): a list of 10 random numbers
            collected from async_generator()
    """
    collection = [i async for i in async_generator()]
    return collection
