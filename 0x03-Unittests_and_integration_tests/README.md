# 0. Parameterize a unit test
A TestAccessNestedMap class that inherits from unittest.TestCase.
The class contains the implementation of the TestAccessNestedMap.test_access_nested_map method
to test that the method returns what it is supposed to.
The method has been decorated with @parameterized.expand to test the function for given inputs

# 1. Parameterize a unit test
Implementing TestAccessNestedMap.test_access_nested_map_exception that uses the assertRaises context
manager to test that a KeyError is raised for a given set of inputs
