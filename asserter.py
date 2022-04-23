from exception import TestFrwException
from result import TestVerdict


class AssertionResult:
    pass


class MetaAsserter(type):
    """To decorate assert_* methods of Asserter."""
    pass


class Asserter(metaclass=MetaAsserter):
    """Mixin for TestCase."""

    def assert_eq(self, measured, expected):
        result = measured == expected
        return result

    def _add_assertion_result(self, assertion_result):
        # todo: Maybe to move this method to MetaAsserter?

        if assertion_result is True:
            self._test_result.update_verdict(TestVerdict.PASSED)
        elif assertion_result is False:
            self._test_result.update_verdict(TestVerdict.FAILED)
        else:
            # In case the assertion_result is not False or True, then, possibly, error?
            # E.g. comparison is not possible because of the obj. types to compare
            #  or comparison methods are not implemented.
            # For now can just throw an exception.
            raise TestFrwException()
