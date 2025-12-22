"""Collection of classes that represent test case(s)."""
import logging

from .checker import Checker
from .result import TestResult

logger = logging.getLogger(__name__)

# to change how TestCase is printed while executing `print(test_result)`
class MetaTestCase(type):
    def __repr__(cls):
        return cls.__name__

class TestCase(Checker, metaclass=MetaTestCase):
    """Abstract test case class."""

    def __new__(cls, *args, **kwargs):
        # avoid Checker instantiation
        # no propagation => no super() call
        return object.__new__(cls)

    def __init__(self, test_result: TestResult):
        # no propagation => no super() call

        # TestResult is attached by runner and used by Checker.
        # Don't use it from TestCase but what returns TestRunner instead.
        self._result = test_result

    def run(self):
        """Abstract test run method.

        User shall implement this method.
        """
        raise NotImplementedError()
