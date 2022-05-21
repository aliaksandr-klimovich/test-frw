"""This module implements classes for collecting and providing test results."""

from enum import IntEnum


CHECK_TEMPLATE = ('args', 'kwargs', 'message', 'result')


class TestVerdict(IntEnum):
    EMPTY = 0  # No assertions were performed. E.g. user forgot to write them.
    SKIPPED = 1  # Test was skipped, not performed.
    PASSED = 2  # Test was successfully run and finished. All assertions returned positive result.
    FAILED = 3  # Test was successfully run and finished. One or more assertions were failed.
    ERROR = 4  # Test was run and threw an exception or error.


class TestResult:
    """
    Test results collector.
    Any test result is collected.
    """

    def __init__(self):
        self.verdict = TestVerdict.EMPTY
        self.stdout = ''
        self.stderr = ''
        self.checks = []

    def update_verdict(self, verdict: TestVerdict):
        """
        This check_method shall be used any time the test_verdict needs to be updated.
        E.g. test verdict is updated any time the check_method or assert_ is made.
        Most "critical" verdict is selected and stored.
        """
        if verdict > self.verdict:
            self.verdict = verdict
