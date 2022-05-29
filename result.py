"""
This module implements classes for collecting and providing test results.
"""

from const import TestVerdict
from logger import log


class TestResult:
    """
    Test results collector.
    """

    def __init__(self):
        self.verdict = TestVerdict.EMPTY
        self.events = []

    def update_verdict(self, verdict: TestVerdict):
        """
        This check_method shall be used any time the test_verdict needs to be updated.
        E.g. test verdict is updated any time the check_method or assert_ is made.
        Most "critical" verdict is selected and stored.
        """
        log.debug(f'update verdict request: {self.verdict.name} -> {verdict.name}')
        if verdict > self.verdict:
            self.verdict = verdict
        log.debug(f'update verdict result: {self.verdict.name}')
