"""Collection of classes that represent test case(s)."""

from checker import Checker

class TestCase(Checker):
    """Abstract test case class."""

    def __new__(cls):
        return object.__new__(cls)

    def run(self):
        """Abstract test run method."""
        raise NotImplementedError()
