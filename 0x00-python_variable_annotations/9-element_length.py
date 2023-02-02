#!/usr/bin/env python3
"""
This module contains a function that takes
an iterable as an argument and returns a list
For instance the iterable can be a list of lists
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes an iterable and finds the element length
    It can take a list of lists and return the length
    of Individual lists (elements), returning
    as a tuple with tuple[0] being the element and
    tuple[1] being the length of the element
    Args:
        lst (iterable[Sequence]): the item to iterate over and
            find the length of individual elements
    Return:
        (list): list of tuples with tuple elements and
        the length of the element
    """
    return [(i, len(i)) for i in lst]
