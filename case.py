from checker import Checker
from result import TestResult


class TestCase(Checker):
    """
    Abstract test case class.
    """

    result: TestResult

    def __init__(self):
        """
        Proto. for initialization.
        Shall not contain any args nor kwargs.
        """
        pass

    def run(self):
        """
        Abstract test run method.
        """
        pass
