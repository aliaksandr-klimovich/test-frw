"""Collection of classes that represent test case(s)."""

from checker import Checker
from result import TestResult


class TestCase(Checker):
    """Abstract test case class."""

    def __init__(self):
        # added by runner
        self.results: list[TestResult] = []

    def run(self):
        """Abstract test run method."""
        pass
