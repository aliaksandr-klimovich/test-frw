"""
To check that basic functionality works.
"""

import unittest

from case import TestCase
from result import TestVerdict
from runner import TestRunner


class TestBasic(unittest.TestCase):
    def test_001_basic(self):
        class MyTestCase(TestCase):
            def run(self):
                self.check_eq(False, True, message='test')
                self.assert_eq(False, True)
                self.assert_eq(True, True)  # not reached

        result = TestRunner.run(MyTestCase)
        self.assertEqual(result.verdict, TestVerdict.FAILED)
        self.assertEqual(
            result.checks,
            [{
                'args': (False, True),
                'kwargs': {},
                'message': 'test',
                'result': False
             },
             {
                'args': (False, True),
                'kwargs': {},
                'message': '',
                'result': False
             }]
        )

    def test_002_fail(self):
        msg = 'from here - manual execution'

        class MyTestCase(TestCase):
            def run(self):
                self.fail(message=msg)
                self.check_eq(True, True)  # not reached

        result = TestRunner.run(MyTestCase)
        self.assertEqual(result.verdict, TestVerdict.FAILED)
        self.assertEqual(result.checks, [{'args': (), 'kwargs': {}, 'message': msg, 'result': False}])


if __name__ == '__main__':
    unittest.main()
