#!/usr/bin/python3
"""This module contains a function that returns the value
of a dictionary key
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T', bound=Any)


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) \
        -> Union[Any, T]:
    """
    This function returns the value of a dictionary key
    Args:
        dct (dict): the dictionary
        key (Any): a key in the dictionary
        default (None): the default
    Return:
        dct[key] (Any): the element in a dictionary key if key present
            else return None
    """
    if key in dct:
        return dct[key]
    else:
        return default
