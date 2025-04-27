"""Classes to group test case(s), suites."""

import logging

from .case import TestCase

log = logging.getLogger(__name__)

class TestSuite:
    """Test cases collector and provider."""

    def __init__(self, *test_cases: type[TestCase]):
        self.test_cases = test_cases

    def add_test_cases(self, *test_cases: type[TestCase]):
        self.test_cases += test_cases

    def get_test_case(self):
        yield from self.test_cases
