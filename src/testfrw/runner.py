"""Classes to run test case(s)."""

import logging

from .case import TestCase
from .events import ErrorEvent
from .exc_info import get_exc_info
from .exceptions import AssertionFail, ComparisonError, TestFrwException
from .result import TestResult, TestVerdict

logger = logging.getLogger(__name__)

class TestRunner:
    """To run test cases.

    It is responsible to:
    1. Create test case instance and test result collector object.
    2. Establish communication channel between test case and test result class.
    3. Return test case run result.
    """

    @staticmethod
    def run1(test_case_class: type[TestCase]) -> TestResult:
        """Run one test case."""

        logger.debug('run1(%s)', test_case_class)

        test_result = TestResult()

        try:
            test_case = test_case_class(test_result)
        except:
            test_result.events.append(ErrorEvent(exc_info=get_exc_info()))
            test_result.update_verdict(TestVerdict.ERROR)
            logger.debug('verdict: %s', test_result.verdict.name)
            return test_result

        # run test case
        try:
            test_case.run()
        except AssertionFail:
            pass
        except ComparisonError:
            pass
        except TestFrwException:
            pass
        except:
            test_result.events.append(ErrorEvent(exc_info=get_exc_info()))
            test_result.update_verdict(TestVerdict.ERROR)
            logger.debug('verdict: %s', test_result.verdict.name)
            return test_result

        del test_case

        logger.debug('verdict: %s', test_result.verdict.name)
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
