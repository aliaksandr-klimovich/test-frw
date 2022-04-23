from typing import Type

from case import TestCase


class TestSuite:
    """Test cases collector."""
    def __init__(self, *test_cases: Type[TestCase]):
        self.test_cases = test_cases
