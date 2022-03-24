from multiprocessing import Process
from typing import Type

from case import TestCase


class TestRunner:
    def __init__(self):
        self.test_cases = []

    def add_test_cases(self, *test_cases: Type[TestCase]):
        self.test_cases += test_cases

    def _run_test_case(self, test_case: Type[TestCase]):
        # create test case instance
        test_case_instance = test_case()
        # execute test function
        test_case_instance.run()

    def run(self):
        for test_case in self.test_cases:
            process = Process(target=self._run_test_case, args=(test_case,))
            process.start()
            process.join()
