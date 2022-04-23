from asserter import Asserter
from result import TestResult


class TestCase(Asserter):
    """Abstract class."""

    def __init__(self):
        self.test_result = TestResult()

    def run(self):
        """Abstract method."""
        pass
