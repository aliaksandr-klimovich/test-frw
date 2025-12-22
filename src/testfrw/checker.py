"""Basic checks collection that test case class may use."""
import logging

from .const import TestVerdict, CheckResult
from .events import FailEvent, Check2Event
from .exceptions import AssertionFail, TestFrwException, ComparisonError
from .result import TestResult

logger = logging.getLogger(__name__)

class Checker:
    """Mixin for TestCase.

    It contains all necessary methods to check and assert entities.
    check_* methods do not fail test case immediately,
    while the assert_* methods do raise an exception that stops test execution.
    """

    _result: TestResult

    def run(self):
        pass

    def fail(self, message=''):
        """Explicitly fail test case run and raise and exception (like assert_* methods do)."""
        if message:
            logger.info(message)
        self._result.events.append(FailEvent(message=message))
        self._result.update_verdict(TestVerdict.FAIL)
        raise AssertionFail()

    @staticmethod
    def _compare_2(actual, sign, expected) -> bool:
        """Compare two objects.

        Args:
            actual: Objects that represents actual data.
            sign: Relation between actual and expected.
            expected: Object that represents expected data.

        Returns:
             Comparison result.

        Raises:
            TestFrwException: in case invalid sign is provided.
            ComparisonError: in case objects cannot be compared.
            Any other error during comparison.
        """
        try:
            if sign == 'eq':
                comparison_result = actual == expected
            elif sign == 'ne':
                comparison_result = actual != expected
            elif sign == 'gt':
                comparison_result = actual > expected
            elif sign == 'ge':
                comparison_result = actual >= expected
            elif sign == 'lt':
                comparison_result = actual < expected
            elif sign == 'le':
                comparison_result = actual <= expected
            elif sign == 'is':
                comparison_result = actual is expected
            elif sign == 'in':
                comparison_result = actual in expected
            elif sign == 'is not':
                comparison_result = actual is not expected
            elif sign == 'not in':
                comparison_result = actual not in expected
            else:
                logger.error('invalid sign: %s', sign, stack_info=False)
                raise TestFrwException()
        except TestFrwException:
            raise
        except:
            logger.error('objects cannot be compared')
            raise ComparisonError()
        return comparison_result

    def _check_2(self, actual, sign, expected, message, strict=False) -> bool:
        """Compare two objects and check result.

        Args:
            actual:
            sign:
            expected:
            message:
            strict:

        Returns:
            Comparison result.
        """
        if message:
            logger.info(message)
        event = Check2Event(actual=actual, sign=sign, expected=expected, message=message, strict=strict)
        self._result.events.append(event)
        comparison_result = None
        try:
            comparison_result = self._compare_2(actual, sign, expected)
        finally:
            if comparison_result is True:
                logger.debug('check result: PASS')
                event.result = CheckResult.PASS
                self._result.update_verdict(TestVerdict.PASS)
            elif comparison_result is False:
                logger.debug('check result: FAIL')
                event.result = CheckResult.FAIL
                self._result.update_verdict(TestVerdict.FAIL)
            else:
                logger.debug('check result: ERROR')
                event.result = CheckResult.ERROR
                self._result.update_verdict(TestVerdict.ERROR)
        return comparison_result

    def _assert_2(self, actual, sign, expected, message):
        result = self._check_2(actual, sign, expected, message, strict=True)
        if result is False:
            raise AssertionFail()

    def check_eq(self, actual, expected, message=''):
        return self._check_2(actual, 'eq', expected, message)

    def assert_eq(self, actual, expected, message=''):
        self._assert_2(actual, 'eq', expected, message)

    def check_ne(self, actual, expected, message=''):
        return self._check_2(actual, 'ne', expected, message)

    def assert_ne(self, actual, expected, message=''):
        self._assert_2(actual, 'ne', expected, message)

    def check_gt(self, actual, expected, message=''):
        return self._check_2(actual, 'gt', expected, message)

    def assert_gt(self, actual, expected, message=''):
        self._assert_2(actual, 'gt', expected, message)

    def check_ge(self, actual, expected, message=''):
        return self._check_2(actual, 'ge', expected, message)

    def assert_ge(self, actual, expected, message=''):
        self._assert_2(actual, 'ge', expected, message)

    def check_lt(self, actual, expected, message=''):
        return self._check_2(actual, 'lt', expected, message)

    def assert_lt(self, actual, expected, message=''):
        self._assert_2(actual, 'lt', expected, message)

    def check_le(self, actual, expected, message=''):
        return self._check_2(actual, 'le', expected, message)

    def assert_le(self, actual, expected, message=''):
        self._assert_2(actual, 'le', expected, message)

    def check_is(self, actual, expected, message=''):
        return self._check_2(actual, 'is', expected, message)

    def assert_is(self, actual, expected, message=''):
        self._assert_2(actual, 'is', expected, message)

    def check_true(self, actual, message=''):
        return self._check_2(actual, 'is', True, message)

    def assert_true(self, actual, message=''):
        self._assert_2(actual, 'is', True, message)

    def check_false(self, actual, message=''):
        return self._check_2(actual, 'is', False, message)

    def assert_false(self, actual, message=''):
        self._assert_2(actual, 'is', False, message)

    def check_none(self, actual, message=''):
        return self._check_2(actual, 'is', None, message)

    def assert_none(self, actual, message=''):
        self._assert_2(actual, 'is', None, message)

    def check_in(self, actual, expected, message=''):
        return self._check_2(actual, 'in', expected, message)

    def assert_in(self, actual, expected, message=''):
        self._assert_2(actual, 'in', expected, message)

    def check_is_not(self, actual, expected, message=''):
        return self._check_2(actual, 'is not', expected, message)

    def assert_is_not(self, actual, expected, message=''):
        self._assert_2(actual, 'is not', expected, message)

    def check_not_in(self, actual, expected, message=''):
        return self._check_2(actual, 'not in', expected, message)

    def assert_not_in(self, actual, expected, message=''):
        self._assert_2(actual, 'not in', expected, message)
