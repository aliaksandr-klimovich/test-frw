"""Classes to run test case(s)."""

import logging

from .case import TestCase
from .events import ErrorEvent
from .exc_info import get_exc_info
from .exceptions import AssertionFail, ComparisonError, TestFrwException
from .hooks import hooks_before_test_run, hooks_after_test_run
from .result import TestResult, TestVerdict

log = logging.getLogger(__name__)

class TestRunner:
    """To run test cases.

    It is responsible to:
    1. Create test case instance and test result collector object.
    2. Establish communication channel between test case and test result class.
    3. Return test case run result.
    """

    @staticmethod
    def run1(test_case_class: type[TestCase], test_result: TestResult = None) -> TestResult:
        """Run one test case."""

        log.info(f'run {test_case_class.__name__}')

        # create test result
        if not test_result:
            test_result = TestResult()

        # create test case instance ?
        try:
            test_case = test_case_class(test_result)
        except:
            test_result.events.append(ErrorEvent(exc_info=get_exc_info()))
            test_result.update_verdict(TestVerdict.ERROR)
            log.info(f'verdict: {test_result.verdict.name}')
            return test_result

        # run fixtures
        # for fixture in test_case_class.__mro__:
        #     if issubclass(fixture, TestCase) and issubclass(fixture, Fixture):
        #         pass  # test case with fixtures
        #     elif issubclass(fixture, TestCase):
        #         pass # test case without fixtures
        #     elif fixture is Fixture:
        #         pass
        #     elif issubclass(fixture, Fixture):
        #         fixture.setup(test_case)

        # run test case
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
            test_result.events.append(ErrorEvent(exc_info=get_exc_info()))
            test_result.update_verdict(TestVerdict.ERROR)
            log.info(f'verdict: {test_result.verdict.name}')
            return test_result

        log.info(f'verdict: {test_result.verdict.name}')
        return test_result

    @classmethod
    def run(cls, test_cases: list[type[TestCase]]):
        """Run multiple test cases.

        todo: What this function shall return?
        """

        # fixtures handling

        tc_tr = [] # temporary

        for test_case in test_cases:
            test_result = TestResult()

            # fixtures handling

            cls.run1(test_case, test_result=test_result)

            tc_tr.append((test_case, test_result))

            # fixtures handling

        # fixtures handling

        return tc_tr
