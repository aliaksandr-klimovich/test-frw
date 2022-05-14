from checker import Checker
from result import TestResult


class TestCase(Checker):
    """Abstract test case class."""

    def __init__(self, test_result: TestResult):
        self._test_result = test_result

    def run(self):
        """Abstract check_method."""
        pass
