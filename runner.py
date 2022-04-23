from multiprocessing import Process
from typing import Type

from case import TestCase


class TestRunner:
    """To run test cases."""

    @staticmethod
    def _run_test_case(test_case: Type[TestCase]):
        """This method runs in separate thread or process."""
        test_case_instance = test_case()
        test_case_instance.run()

    @classmethod
    def run(cls, *test_cases: Type[TestCase]):
        """Runs each test case in a separate process."""
        for test_case in test_cases:
            process = Process(target=cls._run_test_case, args=(test_case,))
            process.start()
            process.join()
