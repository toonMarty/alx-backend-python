#!/usr/bin/env python3
"""
This module contains a class that tests
the access_nested_map method from the module
utils.py
"""
import requests
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import patch, Mock


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

    @parameterized.expand(
        [
            ({}, ('a', 'b')),
            ({'a': 1}, ('a', 'b'))
        ]
    )
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        This method uses the assertRaises context manager to
        test that a KeyError is raised for a given set of
        inputs
        Args:
            nested_map (Mapping): a nested mapping object, eg. a dictionary
            path (Sequence): a sequence object eg. a tuple, list
        Return:
             NoneType
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    This class defines TestGetJson that
    contains a test_get_json method
    """
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    @patch('test_utils.get_json')
    def test_get_json(self, test_url: str, test_payload: Mapping,
                      mock_ret: Dict) -> None:
        """
        This method tests whether get_json returns the expected
        result
        Args:
            mock_ret (Dict): a mock return value
        Return:
             NoneType
        """
        mock_ret.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
