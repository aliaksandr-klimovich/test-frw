from checker import Checker
from result import TestResult


class TestCase(Checker):
    """
    Abstract test case class.
    """

    result: TestResult

    def run(self):
        """
        Abstract test run method.
        """
        pass
