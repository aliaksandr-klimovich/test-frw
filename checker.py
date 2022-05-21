from exception import AssertionFail
from result import TestVerdict, CHECK_TEMPLATE


class MetaChecker(type):
    """
    To decorate check_ methods of Checker class.
    The main purpose of the wrapper is to pass the check_ result to TestResult instance.

    It also creates (generates) similar assert_ methods in Checker class.
    """

    def __new__(mcs, name, bases, namespace):
        if name == 'Checker':
            ns_checks = {}
            ns_asserts = {}
            check_prefix = 'check_'
            assert_prefix = 'assert_'
            for k, v in namespace.items():
                if callable(v) and k.startswith(check_prefix):
                    check_method = mcs._wrap_check(v)
                    ns_checks[k] = check_method
                    assert_method_name = assert_prefix + k[len(check_prefix):]
                    assert_method = mcs._wrap_check2(check_method)
                    ns_asserts[assert_method_name] = assert_method
            namespace.update(ns_checks)
            namespace.update(ns_asserts)
        return type.__new__(mcs, name, bases, namespace)

    def _wrap_check(check_method):
        """Wraps check_ methods of the Checker class."""
        def check_wrapper(self, *args, message='', **kwargs):
            check_results = dict.fromkeys(CHECK_TEMPLATE)
            check_results['args'] = args
            check_results['kwargs'] = kwargs
            check_results['message'] = message
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

    def _wrap_check2(check_method):
        """Wraps _wrap_check methods to produce assert_ methods."""
        def assert_method(*args, **kwargs):
            res = check_method(*args, **kwargs)
            if not res:
                raise AssertionFail()  # todo: Any args/ kwargs to provide to the error instance?
        return assert_method


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
