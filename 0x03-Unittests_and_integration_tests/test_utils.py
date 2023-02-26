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
from typing import Mapping, Sequence, Any
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
    @patch('utils.requests')
    def test_get_json(self, mock_requests: Any) -> None:
        """
        This method tests whether get_json returns the expected
        result
        Args:
            mock_requests (Any): a mock request
        Return:
             NoneType
        """
        mock_response = Mock()
        mock_response.json.return_value = {'payload': False}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_json('http://holberton.io'), {'payload': False})
        mock_requests.get.assert_called_once()

        mock_response_2 = Mock()
        mock_response_2.json.return_value = {'payload': True}
        mock_requests.get.return_value = mock_response_2
        self.assertEqual(get_json('http://example.com'), {'payload': True})
