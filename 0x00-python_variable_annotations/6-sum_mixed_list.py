#!/usr/bin/env python3
"""
This module contains a function that sums the
elements of a list which contains either floats
or int
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function sums elements of a list
    Args:
        mxd_lst (List[Union[float, int]]): a list of elements to be added
    Return:
         result (float): the sum of mxd_list elements
    """
    result: float = 0.0

    for element in mxd_lst:
        result += element

    return result
