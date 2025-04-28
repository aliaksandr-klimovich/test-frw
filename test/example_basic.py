"""This module is for debugging purposes and presents as lightweight example."""

from logger import log

from testfrw.case import TestCase
from testfrw.result import TestResult
from testfrw.runner import TestRunner

class TestCase1(TestCase):
    def run(self):
        self.assert_true(False)

result: TestResult = TestRunner.run1(TestCase1)
log.info(f'test verdict: {result.verdict.name}')
for event in result.events:
    log.info(f'event: {event}')
