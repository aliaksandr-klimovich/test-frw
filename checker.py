"""
This module provides basic checks that test case class should use.
"""

from event import FailEvent, Check2Event, Event
from exception import AssertionFail, TestFrwException, ComparisonError
from logger import log
from const import TestVerdict, CheckResult
from tb_info import get_tb_info


class Checker:
    """
    Mixin for TestCase. It contains all necessary methods to check and assert entities.
    check_ method do not fail test case, while the assert_ methods do raise an exception
    that stops test execution.
    """

    def fail(self, message=''):
        if message:
            log.info(message)
        self._test_result.events.append(FailEvent(message=message))  # noqa
        log.info('set result: FAILED')
        self._test_result.update_verdict(TestVerdict.FAILED)  # noqa
        raise AssertionFail()

    def _compare_2(self, actual, sign, expected, event: Check2Event = None) -> bool:
        try:
            match sign:
                case 'eq': comparison_result = actual == expected
                case 'ne': comparison_result = actual != expected
                case 'gt': comparison_result = actual > expected
                case 'ge': comparison_result = actual >= expected
                case 'lt': comparison_result = actual < expected
                case 'le': comparison_result = actual <= expected
                case 'is': comparison_result = actual is expected
                case 'in': comparison_result = actual in expected
                case 'is not': comparison_result = actual is not expected
                case 'not in': comparison_result = actual not in expected
                case _:
                    log.error(f'invalid sign: "{sign}"', stack_info=False)
                    raise TestFrwException()
        except TestFrwException:
            raise
        except:  # noqa
            # comparison result is undefined

            log.warning('objects cannot be compared')
            # check the exception type, value and stack while in DEBUG log level or in test result -> events

            tb_info = get_tb_info()

            if event:
                event.result = CheckResult.ERROR
                event.tb_info = tb_info

            log.info('check result: ERROR')
            self._test_result.update_verdict(TestVerdict.ERROR)  # noqa

            raise ComparisonError()
        return comparison_result

    def _update_verdict(self, comparison_result: bool, event: Event = None):
        if comparison_result is True:
            if event:
                event.result = CheckResult.PASSED
            log.info('check result: PASSED')
            self._test_result.update_verdict(TestVerdict.PASSED)  # noqa
        elif comparison_result is False:
            if event:
                event.result = CheckResult.FAILED
            log.info('check result: FAILED')
            self._test_result.update_verdict(TestVerdict.FAILED)  # noqa
        else:
            log.warning('comparison result is not a bool value')
            if event:
                event.result = CheckResult.ERROR
            log.info('check result: ERROR')
            self._test_result.update_verdict(TestVerdict.ERROR)  # noqa

    def _check_2(self, actual, sign, expected, message, strict=False):
        event = Check2Event(
            actual=actual,
            sign=sign,
            expected=expected,
            message=message,
            strict=strict
        )
        self._test_result.events.append(event)  # noqa

        if message:
            log.info(message)

        try:
            comparison_result = self._compare_2(actual, sign, expected, event)
        except ComparisonError:
            if strict:  # to reuse this method from similar assert method
                raise
            return None
        else:
            self._update_verdict(comparison_result, event)
        return comparison_result

    def _assert_2(self, actual, sign, expected, message):
        result = self._check_2(actual, sign, expected, message, strict=True)

        if result is True:
            pass
        elif result is False:
            raise AssertionFail()
        else:
            # result is not bool
            #  or the objects cannot be compared
            #  or comparison error is raised
            # however it is checked before in _check_2 method
            # here need to raise an error for assert method call
            raise ComparisonError()

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
        return self._check_2(actual, 'is', True, message)  # noqa

    def assert_true(self, actual, message=''):
        self._assert_2(actual, 'is', True, message)  # noqa

    def check_false(self, actual, message=''):
        return self._check_2(actual, 'is', False, message)  # noqa

    def assert_false(self, actual, message=''):
        self._assert_2(actual, 'is', False, message)  # noqa

    def check_none(self, actual, message=''):
        return self._check_2(actual, 'is', None, message)  # noqa

    def assert_none(self, actual, message=''):
        self._assert_2(actual, 'is', None, message)  # noqa

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
