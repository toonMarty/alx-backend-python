#!/usr/bin/env python3
"""
This module contains a function that
returns the first element of an sequence
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:

    """
    This function finds the first element in a sequence and returns it
    Args:
        lst: a sequence whose elements can be of any type
    Return:
        the first element of the sequence if present else
        return None if sequence is empty
    """
    if lst:
        return lst[0]
    else:
        return None
