"""
This module is for debugging purposes and presented as lightweight example.

To check that basic functionality works.
"""

from case import TestCase
from runner import TestRunner
from log import log


class MyTestCase(TestCase):

    def run(self):

        log.info('checking that failed result is stored and test case does not stuck here')
        self.check_eq(False, True, message='test')

        log.info('checking that failed result leads to aborting test run')
        self.assert_eq(False, True)

        log.info('this log should not be printed')
        self.check_eq(True, True)


result = TestRunner.run(MyTestCase)
log.info(result.verdict)
log.info(result.checks)
