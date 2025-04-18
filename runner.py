"""Classes to run test case(s)."""

from case import TestCase
from events import ErrorEvent
from exc_info import get_exc_info
from exceptions import AssertionFail, ComparisonError, TestFrwException
from hooks import hooks_before_test_run, hooks_after_test_run
from logger import log
from result import TestResult, TestVerdict


class TestRunner:
    """To run test cases.

    It is responsible to:
    1. Create test case instance and test result collector object.
    2. Establish communication channel between test case and test result class.
    3. Return test case run result.
    """

    @staticmethod
    def run1(test_case: TestCase) -> TestResult:
        """Run one test case."""
        log.info(f'run {test_case.__class__.__name__}')
        test_result = TestResult()
        test_case.result = test_result
        try:
            hooks_before_test_run.run(test_case)
            test_case.run()
            hooks_after_test_run.run(test_case)
        except AssertionFail:
            # verdict is updated before the exception is raised
            pass
        except ComparisonError:
            # verdict is updated before the exception is raised
            # log is made before the exception is raised
            pass
        except TestFrwException:
            # log is made before the exception is raised
            pass
        except:
            exc_info = get_exc_info()
            test_result.events.append(ErrorEvent(exc_info=exc_info))
            test_result.update_verdict(TestVerdict.ERROR)
        log.info(f'verdict: {test_result.verdict.name}')
        return test_result

    @classmethod
    def run(cls, test_cases: list[TestCase]) -> list[TestResult]:
        """Run multiple test cases."""
        results = []
        for test_case in test_cases:
            result = cls.run1(test_case)
            results.append(result)
        return results
