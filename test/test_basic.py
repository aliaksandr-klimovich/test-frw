"""
To check basic functionality of the testfrw.
"""
import logging
import sys
import unittest

from case import TestCase
from result import TestVerdict
from runner import TestRunner


log = logging.getLogger('test')
log.setLevel(logging.DEBUG)
_handler = logging.StreamHandler(sys.stdout)
_formatter = logging.Formatter(fmt='[{name}][{levelname}] {message}', style='{')
_handler.setFormatter(_formatter)
log.addHandler(_handler)


class TestBasic(unittest.TestCase):
    def test_basic(self):
        """
        To check that failed check does not stop the test execution.

        First check shall fail.
        Second check (assert) shall fail and stop test execution.
        AssertionError shall not raise.
        Test verdict shall be FAILED.
        """
        class MyTestCase(TestCase):
            def run(self):
                self.check_eq(False, True, message='check False == True')
                self.assert_eq(False, True)
                assert False

        result = TestRunner.run(MyTestCase)
        log.info(result.events)
        self.assertEqual(TestVerdict.FAILED, result.verdict)

    def test_empty_verdict(self):
        """
        To check that in case no check nor assertion is made test verdict does not change,
        i.e. it is initialized as EMPTY and retains its value.
        """
        class MyTestCase(TestCase):
            def run(self):
                pass

        result = TestRunner.run(MyTestCase)
        log.info(result.events)
        self.assertEqual(TestVerdict.EMPTY, result.verdict)

    def test_fail(self):
        """
        To check that can fail test case execution and stop it once `fail` is called.
        The intention here is to leave the rest test execution to user, e.g. manual testing.

        Fail message shall be logged.
        AssertionError shall not raise.
        Test verdict shall be FAILED.
        """

        class MyTestCase(TestCase):
            def run(self):
                self.fail(message='set result to failed and leave test execution')
                assert False  # noqa

        result = TestRunner.run(MyTestCase)
        log.info(result.events)
        self.assertEqual(TestVerdict.FAILED, result.verdict)

    def test_error(self):
        """
        To check that any raised error does not stop test execution.

        AssertionError shall not raise.
        Error message shall be logged.
        Test verdict shall be ERROR.
        """
        class MyTestCase(TestCase):
            def run(self):
                assert False, 'False is not True'

        result = TestRunner.run(MyTestCase)
        log.info(result.events)
        self.assertEqual(TestVerdict.ERROR, result.verdict)

    def test_check_comparison_error(self):
        """
        To check that if any error is raised during comparison,
        test execution continues.

        Object that raises an exception during comparison shall be created.
        Traceback shall be logged.
        Check result shall be None.
        Code after check shall be reached.
        Test verdict shall be ERROR.
        """
        check_result = []
        reached = []

        class CustomException(Exception):
            pass

        class Actual:
            def __eq__(self, other):
                raise CustomException('custom exception message')

        class MyTestCase(TestCase):
            def run(self):
                check_result.append(self.check_eq(Actual(), True))
                reached.append(True)

        result = TestRunner.run(MyTestCase)
        log.info(result.events)
        self.assertEqual([None], check_result)
        self.assertEqual([True], reached)
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

        class MyTestCase(TestCase):
            def run(self):
                self.assert_eq(Actual(), True)
                assert False

        result = TestRunner.run(MyTestCase)
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
        Code after first check shall be reached.
        Check result shall be None.
        Test verdict shall be ERROR.
        """
        actual = object()
        expected = object()
        check_result = []
        reached = []

        class MyTestCase(TestCase):
            def run(self):
                check_result.append(self.check_gt(actual, expected))
                reached.append(True)

        result = TestRunner.run(MyTestCase)
        log.info(result.events)
        self.assertEqual([None], check_result)
        self.assertEqual([True], reached)
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

        class MyTestCase(TestCase):
            def run(self):
                self.assert_gt(actual, expected, message='check objects cannot be compared')
                assert False

        result = TestRunner.run(MyTestCase)
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

        class MyTestCase(TestCase):
            def run(self):
                check_result.append(self.check_eq(Actual(), True))
                reached.append(True)

        result = TestRunner.run(MyTestCase)
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

        class MyTestCase(TestCase):
            def run(self):
                self.assert_eq(Actual(), True)
                assert False

        result = TestRunner.run(MyTestCase)
        log.info(result.events)
        self.assertEqual(TestVerdict.ERROR, result.verdict)

    def test_check_true(self):
        """
        To check verdict update process.
        """

        class MyTestCase(TestCase):
            def run(self):
                self.check_true(True)
                self.check_true(False)
                self.check_true(True)

        result = TestRunner.run(MyTestCase)
        log.info(result.events)
        self.assertEqual(TestVerdict.FAILED, result.verdict)


if __name__ == '__main__':
    unittest.main()
