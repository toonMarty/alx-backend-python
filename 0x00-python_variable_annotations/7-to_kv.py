#!/usr/bin/env python3
"""
This module contains a function that takes two arguments
a string and a number either float or int and converts or
packs them to a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function packs two individual types, a string and
    a number to a tuple with a key-value pair where the string
    is the key and the number is the tuple
    Args:
        k (str): the str
        v (int, float): a number that is either an int or a
            float
    Return:
        square (tuple): a key-value tuple of k and v
    """
    square: float = v * v
    return k, square
