"""
This module is for debugging purposes and presented as lightweight example.
"""

from case import TestCase
from runner import TestRunner


class MyTestCase(TestCase):
    def run(self):
        print('checking that failed result is stored and test case does not stuck here')
        self.check_eq(False, True, message='test')

        print('checking that failed result leads to aborting test run')
        self.assert_eq(False, True)

        print('this log should not be printed')
        self.check_eq(True, True)


result = TestRunner.run(MyTestCase)
assert result.verdict.name == 'FAILED'
