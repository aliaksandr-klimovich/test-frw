# Documentation

## Requirements

- Test is written and located in TestCase class.
- Each test case should contain only one test to run, i.e. only one meaningful test entity.
- TestCase should contain a method that starts the test. 
  Test is started outside TestCase class.
- A tool to run TestCase should be implemented, i.e. TestRunner class.
- TestRunner should run test(s) in an isolated environment, i.e. thread or process.
- (?) API for TestCase and TestRunner should be implemented to have possibility to extend these classes.
- TestResult class should be implemented. It shall contain information about test case run results.
- TestRunner should return TestResult after TestCase execution.
- TestLoader should be implemented to locate test cases and pass them to TestRunner.
- TestSuite should be implemented to group tests.
- (?) After test run TestCase should be destroyed and resources should be released.
- (?) TestCase should contain TestResult as a property.
- Should be possibility to parametrize test case.
- Should be possibility to run tests in parallel.
- There should be methods to assert and check entities.
  Assert should cause test fail immediately.
  Check should store failed result, continue test execution and at the end of the test fail it.
