"""
To check basic functionality of the test_frw.
"""

import logging
import unittest

from case import TestCase
from logger import handler as _handler
from result import TestVerdict
from runner import TestRunner

log = logging.getLogger('test')
log.setLevel(logging.DEBUG)
log.addHandler(_handler)


class TestChecksAndAssertions(unittest.TestCase):
    def test_empty_verdict(self):
        """
        To check that in case no check nor assertion is made test verdict does not change,
        i.e. it is initialized as EMPTY and retains its value.
        """

        class CustomTestCase(TestCase):
            def run(self):
                pass

        result = TestRunner.run1(CustomTestCase)
        log.debug(result.events)
        self.assertEqual(result.verdict, TestVerdict.EMPTY)

    def test_check_positive(self):
        """
        To check that calling check_* results in passed test case.
        """

        class CustomTestCase(TestCase):
            def run(self):
                self.check_eq(True, True)

        result = TestRunner.run1(CustomTestCase)
        log.debug(result.events)
        self.assertEqual(result.verdict, TestVerdict.PASS)

    def test_assert_positive(self):
        """
        To check that calling assert_* results in passed test case.
        """

        class CustomTestCase(TestCase):
            def run(self):
                self.assert_eq(True, True)

        result = TestRunner.run1(CustomTestCase)
        log.debug(result.events)
        self.assertEqual(result.verdict, TestVerdict.PASS)

    def test_check_does_not_stop_test_execution(self):
        """
        To check that failed check does not stop test execution.

        Check shall fail but test shall continue.
        Test verdict shall be FAIL.
        """
        reached = []

        class CustomTestCase(TestCase):
            def run(self):
                self.check_eq(False, True, message='check False == True')
                reached.append(True)

        result = TestRunner.run1(CustomTestCase)
        log.debug(result.events)
        self.assertEqual(reached, [True])
        self.assertEqual(result.verdict, TestVerdict.FAIL)

    def test_check_comparison_error(self):
        """
        To check that if any error is raised during comparison,
        test execution does not continue.

        Object that raises an exception during comparison shall be created.
        Traceback shall be logged.
        Check result shall be empty.
        Code after check shall not be reached.
        Test verdict shall be ERROR.
        """
        check_result = []
        reached = []

        class CustomException(Exception):
            pass

        class Actual:
            def __eq__(self, other):
                raise CustomException('custom exception message')

        class CustomTestCase(TestCase):
            def run(self):
                check_result.append(self.check_eq(Actual(), True))
                reached.append(True)

        result = TestRunner.run1(CustomTestCase)
        log.info(result.events)
        self.assertEqual([], check_result)
        self.assertEqual([], reached)
        self.assertEqual(TestVerdict.ERROR, result.verdict)

    def test_assert_comparison_error(self):
        """
        To check that if any error is raised during comparison
        test execution stops.

        Object that raises an exception during comparison shall be created.
        Traceback shall be logged.
        AssertionError shall not raise.
        Test verdict shall be ERROR.
        """

        class CustomException(Exception):
            pass

        class Actual:
            def __eq__(self, other):
                raise CustomException('custom exception message')

        class CustomTestCase(TestCase):
            def run(self):
                self.assert_eq(Actual(), True)
                assert False

        result = TestRunner.run1(CustomTestCase)
        log.info(result.events)
        self.assertEqual(TestVerdict.ERROR, result.verdict)

    def test_check_cannot_compare_objects(self):
        """
        To check that two objects that cannot be compared in python
        (because proper methods are not implemented
         or the comparison returns non-bool value)
        do not stop the test execution.

        Two objects shall be created, `__gt__` method shall not be implemented there.
        Traceback shall be logged.
        Code after first check shall not be reached.
        Check result shall be empty.
        Test verdict shall be ERROR.
        """
        actual = object()
        expected = object()
        check_result = []
        reached = []

        class CustomTestCase(TestCase):
            def run(self):
                check_result.append(self.check_gt(actual, expected))
                reached.append(True)

        result = TestRunner.run1(CustomTestCase)
        log.info(result.events)
        self.assertEqual([], check_result)
        self.assertEqual([], reached)
        self.assertEqual(TestVerdict.ERROR, result.verdict)

    def test_assert_cannot_compare_objects(self):
        """
        To check that two objects that cannot be compared in python
        (because proper methods are not implemented
         or the comparison returns non-bool value)
        stop the test execution.

        Two objects shall be created, `__gt__` method shall not be implemented there.
        Traceback shall be logged.
        AssertionError shall not raise.
        Test verdict shall be ERROR.
        """
        actual = object()
        expected = object()

        class CustomTestCase(TestCase):
            def run(self):
                self.assert_gt(actual, expected, message='check objects cannot be compared')
                assert False

        result = TestRunner.run1(CustomTestCase)
        log.info(result.events)
        self.assertEqual(TestVerdict.ERROR, result.verdict)

    def test_check_result_is_not_a_bool_value(self):
        """
        To check that in case the comparison result is not a bool value
        test execution does not stop.

        Two objects shall be created, __eq__ method shall return 1 at least by first object.
        Warning shall be logged.
        Check result shall be 1.
        Code after check shall be reachable.
        Test verdict shall be ERROR.
        """
        check_result = []
        reached = []

        class Actual:
            def __eq__(self, other):
                return 1

        class CustomTestCase(TestCase):
            def run(self):
                check_result.append(self.check_eq(Actual(), True))
                reached.append(True)

        result = TestRunner.run1(CustomTestCase)
        log.info(result.events)
        self.assertEqual([1], check_result)
        self.assertEqual([True], reached)
        self.assertEqual(TestVerdict.ERROR, result.verdict)

    def test_assert_result_is_not_a_bool_value(self):
        """
        To check that in case the comparison result is not a bool value
        test execution stops.

        Two objects shall be created, __eq__ method shall return 1 at least by first object.
        Warning shall be logged.
        AssertionError shall not raise.
        Test verdict shall be ERROR.
        """

        class Actual:
            def __eq__(self, other):
                return 1

        class CustomTestCase(TestCase):
            def run(self):
                self.assert_eq(Actual(), True)
                assert False

        result = TestRunner.run1(CustomTestCase)
        log.info(result.events)
        self.assertEqual(TestVerdict.ERROR, result.verdict)

    def test_check_true(self):
        """
        To check verdict update process.
        """

        class CustomTestCase(TestCase):
            def run(self):
                self.check_true(True)
                self.check_true(False)
                self.check_true(True)

        result = TestRunner.run1(CustomTestCase)
        log.info(result.events)
        self.assertEqual(TestVerdict.FAIL, result.verdict)


class TestFail(unittest.TestCase):
    def test_fail(self):
        """
        To check that can fail test case execution and stop it once `fail` method is called.
        The intention here is to leave the rest test execution to user, e.g. manual testing.

        Fail message shall be logged.
        AssertionError shall not raise.
        Test verdict shall be FAIL.
        """
        reached = []

        class CustomTestCase(TestCase):
            def run(self):
                self.fail(message='set result to failed and leave test execution')
                reached.append(True)  # noqa

        result = TestRunner.run1(CustomTestCase)
        log.debug(result.events)
        self.assertEqual(reached, [])
        self.assertEqual(result.verdict, TestVerdict.FAIL)


class TestInitAndRun(unittest.TestCase):
    def test_init_error(self):
        """
        To check situation when test case init fails.
        """

        class CustomTestCase(TestCase):
            def __init__(self):  # noqa
                raise RuntimeError()

        result = TestRunner.run1(CustomTestCase)
        log.debug(result.events)
        self.assertEqual(result.verdict, TestVerdict.ERROR)

    def test_run_error(self):
        """
        To check that any error during test run does not crush test execution.

        Error message shall be logged.
        Test verdict shall be ERROR.
        """
        true = True  # to see it in exc_tb log

        class CustomTestCase(TestCase):
            def run(self):
                assert False, f'False is not {true}'

        result = TestRunner.run1(CustomTestCase)
        log.debug(result.events)
        self.assertEqual(TestVerdict.ERROR, result.verdict)


if __name__ == '__main__':
    unittest.main()
