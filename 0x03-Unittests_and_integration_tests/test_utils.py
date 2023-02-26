#!/usr/bin/env python3
"""
This module contains a class that tests
the access_nested_map method from the module
utils.py
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    This class defines the test_method that uses
    the parameterized expand decorator
    """
    @parameterized.expand(
        [({"a": 1}, ("a", ), 1),
         ({"a": {"b": 2}}, ("a", ), {"b": 2}),
         ({"a": {"b": 2}}, ("a", "b"), 2)
         ]
    )
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """
        This method tests that access_nested_map method returns what
        it is supposed to return
        Args:
            nested_map(Mapping): first input, a nested dictionary
            path(Sequence): second input, a sequence object
            expected(Any): the expected output given the two
                parameters as inputs
        Return:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
