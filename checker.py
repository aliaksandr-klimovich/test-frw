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

    # def check_true(self, measured, message=''):
    #     return measured is True
    #
    # def assert_true(self, measured, message=''):
    #     """stub"""
    #
    # def check_false(self, measured, message=''):
    #     return measured is False
    #
    # def assert_false(self, measured, message=''):
    #     """stub"""
    #
    # def check_is(self, measured, expected, message=''):
    #     return measured is expected
    #
    # def assert_is(self, measured, expected, message=''):
    #     """stub"""

    def fail(self, message=''):
        log.info(f'message: {message}')
        self._test_result.update_verdict(TestVerdict.FAILED)  # noqa
        raise AssertionFail()

    def _compare_2(self, actual, sign, expected):
        try:
            match sign:
                case 'eq':  result = actual == expected
                case 'neq': result = actual != expected
                case 'is':  result = actual is expected
                case 'gt':  result = actual > expected
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

    def _check_2(self, actual, sign: str, expected, message='', strict=False):
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

    def check_eq(self, actual, expected, message=''):
        return self._check_2(actual, 'eq', expected, message)

    def check_gt(self, actual, expected, message=''):
        return self._check_2(actual, 'gt', expected, message)

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

    def assert_eq(self, actual, expected, message=''):
        self._assert_2(actual, 'eq', expected, message)

    def assert_gt(self, actual, expected, message=''):
        self._assert_2(actual, 'gt', expected, message)
