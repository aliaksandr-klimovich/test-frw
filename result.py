"""
This module implements classes for collecting and providing test results.
"""

from const import TestVerdict
from events import Event
from logger import log


class TestResult:
    """
    Test results collector.
    """

    verdict: TestVerdict
    events: list[Event]

    def __init__(self):
        self.verdict = TestVerdict.EMPTY
        self.events = []

    def update_verdict(self, verdict: TestVerdict):
        """
        This method shall be used any time the test verdict needs to be updated.
        E.g. test verdict is updated any time the check_* method or assert_* is made.
        Most critical verdict is selected and stored.
        """
        if verdict > self.verdict:
            log.debug(f'verdict: {self.verdict.name} -> {verdict.name}')
            self.verdict = verdict
        else:
            log.debug(f'verdict: {self.verdict.name}')
