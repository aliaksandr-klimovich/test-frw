"""This module provides classes to run test cases."""

from typing import Type

from case import TestCase
from exception import AssertionFail
from result import TestResult, TestVerdict


class TestRunner:
    """
    To run test cases.

    It is responsible to:
    1. Create test case instance and test result collector object.
    2. Establish communication channel between test case and test result class.
    3. Return test case run result.
    """

    @classmethod
    def run(cls, test_case: Type[TestCase]):

        test_result = TestResult()

        test_case_instance = test_case(test_result=test_result)
        try:
            test_case_instance.run()
        except AssertionFail:
            test_result.update_verdict(TestVerdict.FAILED)
        except:
            test_result.update_verdict(TestVerdict.ERROR)
            # todo: Get traceback.
            raise  # todo: Do not fail test run. Currently left for debug purposes.

        del test_case_instance  # todo: Is this a good idea?

        return test_result
