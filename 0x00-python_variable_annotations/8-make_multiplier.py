#!/usr/bin/env python3
"""
This module contains a function that takes a float
multiplier and returns a function that multiplies a
float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a multiplier of type float
    Args:
        multiplier (float): the number to multiply by
    Return:
        product (Callable): a function which is the product
            of a float and a multiplier
    """
    def product(multiplicand: float):
        """
        This function multiplies the multiplier from
        the outer function and a multiplicand
        Args:
            multiplicand (float): will be multiplied by
                the multiplier
        Return:
            multiplier * multiplicand (float): the product
        """
        return multiplier * multiplicand
    return product
