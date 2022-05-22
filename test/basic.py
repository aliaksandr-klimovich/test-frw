"""
To check basic functionality of the testfrw.
"""

import unittest

from case import TestCase
from result import TestVerdict
from runner import TestRunner


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
                self.check_eq(False, True, message='test')
                self.assert_eq(False, True)
                assert False

        result = TestRunner.run(MyTestCase)
        self.assertEqual(TestVerdict.FAILED, result.verdict, )

    def test_empty_verdict(self):
        """
        To check that in case no check nor assertion is made test verdict does not change,
        i.e. it is initialized as EMPTY and retains its value.
        """
        class MyTestCase(TestCase):
            def run(self):
                pass

        result = TestRunner.run(MyTestCase)
        self.assertEqual(TestVerdict.EMPTY, result.verdict, )

    def test_fail(self):
        """
        To check that can fail test case execution and stop it once `fail` is called.
        The intention here is to leave the rest test execution to user, e.g. manual testing.

        Fail message shall be logged.
        AssertionError shall not raise.
        Test verdict shall be FAILED.
        """
        message = 'manual execution from here'

        class MyTestCase(TestCase):
            def run(self):
                self.fail(message=message)
                assert False

        result = TestRunner.run(MyTestCase)
        # todo: check log message
        self.assertEqual(TestVerdict.FAILED, result.verdict, )

    def test_error(self):
        """
        To check that any raised error does not stop test execution.

        AssertionError shall not raise.
        Error message shall be logged.
        Test verdict shall be ERROR.
        """
        class MyTestCase(TestCase):
            def run(self):
                assert False

        result = TestRunner.run(MyTestCase)
        # todo: check traceback
        self.assertEqual(TestVerdict.ERROR, result.verdict, )

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
                raise CustomException()

        class MyTestCase(TestCase):
            def run(self):
                check_result.append(self.check_eq(Actual(), True))
                reached.append(True)

        result = TestRunner.run(MyTestCase)
        # todo: check traceback
        self.assertEqual([None], check_result)
        self.assertEqual([True], reached)
        self.assertEqual(TestVerdict.ERROR, result.verdict, )

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
                raise CustomException()

        class MyTestCase(TestCase):
            def run(self):
                self.assert_eq(Actual(), True)
                assert False

        result = TestRunner.run(MyTestCase)
        self.assertEqual(TestVerdict.ERROR, result.verdict, )

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
        # todo: check traceback
        self.assertEqual([None], check_result)
        self.assertEqual([True], reached)
        self.assertEqual(TestVerdict.ERROR, result.verdict, )

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
                self.assert_gt(actual, expected)
                assert False

        result = TestRunner.run(MyTestCase)
        # todo: check traceback
        self.assertEqual(TestVerdict.ERROR, result.verdict, )

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
        # todo: check warning
        self.assertEqual([1], check_result)
        self.assertEqual([True], reached)
        self.assertEqual(TestVerdict.ERROR, result.verdict, )

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
        # todo: check warning
        self.assertEqual(TestVerdict.ERROR, result.verdict, )

    def test_check_true(self):
        # todo: write description
        class MyTestCase(TestCase):
            def run(self):
                self.check_true(True)

        result = TestRunner.run(MyTestCase)
        self.assertEqual(TestVerdict.PASSED, result.verdict)


if __name__ == '__main__':
    unittest.main()
