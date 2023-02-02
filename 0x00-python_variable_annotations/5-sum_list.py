#!/usr/bin/env python3
"""
This module contains a function that sums
the elements of a list which are of type float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This functions sums the elements of a list
    Args:
        input_list (List[float]): a list of float values
    Return:
         result (float): the sum of the list elements
    """
    result: float = 0.0
    for float_element in input_list:
        result += float_element
    return result
