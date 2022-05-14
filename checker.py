from functools import wraps

from exception import AssertionFail
from result import TestVerdict, CHECK_TEMPLATE


class MetaChecker(type):
    """To decorate assert_ and check_ methods of Checker class."""

    def __new__(mcs, name, bases, namespace):
        if name == 'Checker':
            for k, v in namespace.items():
                if callable(v):
                    if k.startswith('check_'):
                        namespace[k] = MetaChecker._wrap_check(v)
                    elif k.startswith('assert_'):
                        namespace[k] = MetaChecker._wrap_assert(v)
        return type.__new__(mcs, name, bases, namespace)

    def _wrap_check(check_method):
        """Wraps all check_ methods."""
        @wraps(check_method)
        def check_wrapper(self, *args, **kwargs):
            check_results = dict.fromkeys(CHECK_TEMPLATE)
            check_results['args'] = args
            check_results['kwargs'] = kwargs
            self._test_result.checks.append(check_results)
            try:
                check_result = check_method(self, *args, **kwargs)
            except:
                # todo:
                #  What to do in case the objects cannot be compared and this method raises an Exception?
                #  Need to handle this exception.
                raise
            check_results['result'] = check_result
            if check_result is True:
                self._test_result.update_verdict(TestVerdict.PASSED)
            elif check_result is False:
                self._test_result.update_verdict(TestVerdict.FAILED)
            else:
                # todo: Handle invalid check_result.
                pass
            return check_result
        return check_wrapper

    def _wrap_assert(assert_method):
        """Wraps all assert_ methods."""
        @wraps(assert_method)
        def assert_wrapper(self, *args, **kwargs):
            check_results = dict.fromkeys(CHECK_TEMPLATE)
            check_results['args'] = args
            check_results['kwargs'] = kwargs
            self._test_result.checks.append(check_results)
            try:
                assert_method(self, *args, **kwargs)
            # except AssertionFail:
            #     check_results['result'] = False
            #     # verdict will be updated by TestRunner
            #     raise
            except:
                check_results['result'] = False
                # verdict will be updated by TestRunner
                raise
            else:
                check_results['result'] = True
                self._test_result.update_verdict(TestVerdict.PASSED)
        return assert_wrapper


class Checker(metaclass=MetaChecker):
    """
    Mixin for TestCase. It contains all necessary methods to check and assert entities.
    check_ method do not fail test case, while the assert_ methods do raise an exception.
    """

    def check_eq(self, measured, expected, message=''):
        return measured == expected

    def assert_eq(self, measured, expected, message=''):
        if not measured == expected:
            raise AssertionFail(measured, expected, message=message)
