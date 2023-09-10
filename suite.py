"""
This module provides classes to group test cases.
"""

from typing import Type

from case import TestCase


class TestSuite:
    """
    Test cases collector and provider.
    """

    def __init__(self, *test_cases: Type[TestCase]):
        self.test_cases = test_cases

    def add_test_cases(self, *test_cases: Type[TestCase]):
        self.test_cases += test_cases

    def get_test_case(self):
        yield from self.test_cases
