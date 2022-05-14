"""This module provides classes to run test cases."""

import sys
from io import StringIO
from typing import Type

from case import TestCase
from exception import AssertionFail
from result import TestResult, TestVerdict

_orig_stdout = sys.stdout
_orig_stderr = sys.stderr


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

        # todo: Support live log.

        stdout = StringIO()
        stderr = StringIO()

        sys.stdout = stdout
        sys.stderr = stderr

        test_result = TestResult()

        test_case_instance = test_case(test_result=test_result)
        try:
            test_case_instance.run()
        except AssertionFail:
            test_result.update_verdict(TestVerdict.FAILED)
        except:
            test_result.update_verdict(TestVerdict.ERROR)
            # todo: Get traceback.

        del test_case_instance  # todo: Is this a good idea?

        stdout.seek(0)
        test_result.stdout = stdout.read()
        stderr.seek(0)
        test_result.stderr = stderr.read()

        stdout.close()
        del stdout
        stderr.close()
        del stderr

        sys.stdout = _orig_stdout
        sys.stderr = _orig_stderr

        return test_result


class ThreadTestRunner:
    pass


class ProcessTestRunner:
    pass
