from exception import AssertionFail, TestFrwException
from log import log
from result import TestVerdict


class Checker:
    """
    Mixin for TestCase. It contains all necessary methods to check and assert entities.
    check_ method do not fail test case, while the assert_ methods do raise an exception.
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
    #     """stud"""
    #
    # def check_is(self, measured, expected, message=''):
    #     return measured is expected
    #
    # def assert_is(self, measured, expected, message=''):
    #     """stub"""

    @staticmethod
    def _log_check_setup(actual, expected, message):
        log.info(message)
        log.info(f'actual: {actual}')
        log.info(f'expected: {expected}')

    @staticmethod
    def _log_verdict(verdict):
        log.info(f'verdict: {verdict.name}')

    @staticmethod
    def _log_cannot_compare():
        log.info('objects cannot be compared: comparison result is not a bool value')

    @staticmethod
    def _log_comparison_error():
        log.info('objects cannot be compared: error is raised while comparing objects')

    def _compare_with_try_2(self, actual, sign, expected, ):
        try:
            if sign == '==':
                result = actual == expected
            elif sign == '!=':
                result = actual != expected
            elif sign == 'is':
                result = actual is expected
            else:
                raise TestFrwException(f'Invalid sign: "{sign}".')
        except:
            # error is raised during comparison
            # e.g. objects cannot be compared
            self._log_comparison_error()
            result = False
            # todo: update verdict?
        return result

    def _update_verdict(self, result: bool) -> bool:
        if result is True:
            verdict = TestVerdict.PASSED
            self._log_verdict(verdict)
            self._test_result.update_verdict(verdict)
        elif result is False:
            verdict = TestVerdict.FAILED
            self._log_verdict(verdict)
            self._test_result.update_verdict(verdict)
        else:
            # result is not a bool value
            self._log_cannot_compare()
            result = False
            # todo: update verdict?
        return result

    def check_eq(self, actual, expected, message=''):
        self._log_check_setup(actual, expected, message)
        result = self._compare_with_try_2(actual, '==', expected)
        result = self._update_verdict(result)
        return result

    def assert_eq(self, actual, expected, message=''):
        if self.check_eq(actual, expected, message) is False:
            raise AssertionFail()
        return True

    # def fail(self, message=''):
    #     check_results = dict.fromkeys(CHECK_TEMPLATE)
    #     check_results['args'] = ()
    #     check_results['kwargs'] = {}
    #     check_results['message'] = message
    #     check_results['result'] = False
    #     self._test_result.checks.append(check_results)
    #     self._test_result.update_verdict(TestVerdict.FAILED)
    #     raise AssertionFail()
