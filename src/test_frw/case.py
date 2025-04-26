"""Collection of classes that represent test case(s)."""
import logging

from .checker import Checker

log = logging.getLogger(__name__)

# just to change how TestCase is printed while executing `print(test_result)`
class MetaTestCase(type):
    def __repr__(cls):
        return cls.__name__

class TestCase(Checker, metaclass=MetaTestCase):
    """Abstract test case class."""

    def __new__(cls, *args, **kwargs):
        # no propagation => no super() call
        return object.__new__(cls)

    def __init__(self, test_result):
        # no propagation => no super() call

        # result attached by runner. used by checker.
        # don't use it. use what returns runner instead.
        self.result = test_result

    def run(self):
        """Abstract test run method.

        User shall implement this method.
        """
        raise NotImplementedError()
