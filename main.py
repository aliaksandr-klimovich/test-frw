"""
Requirements
------------

- Test is written and located in TestCase class.

  [*] Design constrain.
  [v] TestCase class implemented.

- Each test case should contain only one test to run, i.e. only one meaningful test entity.

  [*] Design constrain.

- TestCase should contain a method that starts the test. Test is started outside TestCase class.

  [v] TestCase class contains "run" method. Children class should implement it.
  [ ] TestCase contains method name to run. This name is used to start test case.
      By default, "run" method is used.

- A tool to run TestCase should be implemented, i.e. TestRunner class.

  [v] TestRunner class implemented. It is a container for test cases to run.
      It contains "add_test_cases" method to collect TestCase(s).
      Run is made by iterating over test cases and running each test case one by one.

- TestRunner should run test(s) in an isolated environment, i.e. thread or process.

  [v] Implemented in TestRunner class to run test cases.

- API for TestCase and TestRunner should be implemented to have possibility to extend these classes.

  [ ]

- TestResult class should be implemented. It shall contain information about test case run results.

- TestRunner should return TestResult after TestCase execution.

- TestLoader should be implemented to locate test cases and pass them to TestRunner.

  [ ] TestLoader implemented.

- TestSuite should be implemented to group tests.

  [ ] TestSuite implemented.

- (?) After test run TestCase should be destroyed and resources should be released.

- (?) TestCase should contain TestResult as a property.

- Should be possibility to parametrize test case.

- Should be possibility to run tests in parallel.

- There should be methods to assert and check entities.
  Assert should cause test fail immediately.
  Check should store failed result, continue test execution and at the end of the test fail it.
"""
from multiprocessing import Process
from typing import Type


class TestCase:
    def run(self):
        pass

    def assert_equals(self, measured, expected):
        result = measured == expected
        return result


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
