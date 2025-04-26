"""This module is for debugging purposes and presents as lightweight example."""

from test_frw.case import TestCase
from test_frw.result import TestResult
from test_frw.runner import TestRunner

from logger import log

class TestCase1(TestCase):
    def run(self):
        self.assert_true(False)

result: TestResult = TestRunner.run1(TestCase1)
log.info(f'test verdict: {result.verdict.name}')
for event in result.events:
    log.info(f'event: {event}')
