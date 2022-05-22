"""
This module provides basic checks that test case class should use.
"""

from exception import AssertionFail, TestFrwException, ComparisonError
from log import log
from result import TestVerdict


class Checker:
    """
    Mixin for TestCase. It contains all necessary methods to check and assert entities.
    check_ method do not fail test case, while the assert_ methods do raise an exception
    that stops test execution.
    """

    def fail(self, message=''):
        log.info(f'message: {message}')
        self._test_result.update_verdict(TestVerdict.FAILED)  # noqa
        raise AssertionFail()

    def _compare_2(self, actual, sign, expected):
        try:
            match sign:
                case 'eq': result = actual == expected
                case 'neq': result = actual != expected
                case 'gt': result = actual > expected
                case 'ge': result = actual >= expected
                case 'lt': result = actual < expected
                case 'le': result = actual <= expected
                case 'is': result = actual is expected
                case 'in': result = actual in expected
                case 'not is': result = not(actual is expected)
                case 'not in': result = actual not in expected
                case _:
                    log.error(f'invalid sign: {sign}')
                    raise TestFrwException()
        except TestFrwException:
            raise
        except:  # noqa
            log.info('objects cannot be compared: error is raised while comparing objects')
            self._test_result.update_verdict(TestVerdict.ERROR)  # noqa
            # result cannot be obtained in this case
            # todo:
            #  log.error or log.debug with traceback
            #  since this is not a frw error, log.debug is more suitable
            raise ComparisonError()
        else:
            log.info(f'check result: {result}')
        return result

    def _update_verdict(self, result):
        if result is True:
            self._test_result.update_verdict(TestVerdict.PASSED)  # noqa
        elif result is False:
            self._test_result.update_verdict(TestVerdict.FAILED)  # noqa
        else:
            log.warning('check result is not a bool value')
            self._test_result.update_verdict(TestVerdict.ERROR)  # noqa

    def _check_2(self, actual, sign, expected, message, strict=False):
        log.info(f'message: {message}')
        log.info(f'actual: {actual}')
        log.info(f'expected: {expected}')
        try:
            result = self._compare_2(actual, sign, expected)
        except ComparisonError:
            if strict:  # to reuse this method from similar assert method
                raise
            return None
        else:
            self._update_verdict(result)
        return result

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
            raise ComparisonError()

    def check_eq(self, actual, expected, message=''):
        return self._check_2(actual, 'eq', expected, message)

    def assert_eq(self, actual, expected, message=''):
        self._assert_2(actual, 'eq', expected, message)

    def check_neq(self, actual, expected, message=''):
        return self._check_2(actual, 'neq', expected, message)

    def assert_neq(self, actual, expected, message=''):
        self._assert_2(actual, 'neq', expected, message)

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

    def check_not_is(self, actual, expected, message=''):
        return self._check_2(actual, 'not is', expected, message)

    def assert_not_is(self, actual, expected, message=''):
        self._assert_2(actual, 'not is', expected, message)

    def check_not_in(self, actual, expected, message=''):
        return self._check_2(actual, 'not in', expected, message)

    def assert_not_in(self, actual, expected, message=''):
        self._assert_2(actual, 'not in', expected, message)


