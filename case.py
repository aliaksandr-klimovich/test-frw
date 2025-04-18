"""Collection of classes that represent test case(s)."""

from checker import Checker
from result import TestResult


class TestCase(Checker):
    """Abstract test case class."""

    result: TestResult  # attached by runner

    def run(self):
        """Abstract test run method."""
        pass
