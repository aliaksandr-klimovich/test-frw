# Documentation

## Requirements

### General considerations

- Implementation shall be simple to understand and use.
- Any part of the code shall be easy to modify and extended.
- Shall be implemented in pure python. 
  No external packages shall be used (`requirements.txt` shall be empty).

User is responsible for:
- Steams handling: stdout and stderr. 
- Configure logger.

This document marks:
- Lines marked with (?) are questionable/ under development/ clarification.
- Lines marked with (!) are to pay attention to/ may not be implemented yet.

### Entities

#### TestVerdict

- Enumeration, defines test verdict of one test execution.

#### Event

- Base event implementation.
- Holds timestamp when it was created.
- (!) Shall provide subscription interface.
- Shall occur on different actions of other `test_frw` entities.
  Any significant action is considered an event and shall be stored in `TestResult`.
  (?) ToDo: define when.

#### Hook

(?)

#### TestCase

- Entity that contains one test to execute.
- Should contain all necessary information (variables, methods, etc.) to run the test.
  User shall inherit from `TestCase` class and implement `run` method. 
- Shall contain `run` method. This method shall be used by `test_frw` to start test execution.
- Shall contain methods to _assert_ and _check_:
    - _Assert_ shall cause test fail immediately (`AssertionFail`).
    - _Check_ method shall:
        - store failed result,
        - continue test execution,
    - Both methods shall update `TestVerdict` accordingly.
- (!) Should be possibility to parametrize `TestCase`.

#### TestResult

- Container that contains all information about test execution.
- Shall contain `TestVerdict`.
- Shall contain checks and assertions results.
- Stores Events occurred during test execution. 
- (?)Should provide test output.

#### TestRunner

- Should run `TestCase` in an isolated environment.
- Shall create instance of the `TestCase`.
- Shall create instance of the `TestResult`.
- (?) Should bind `TestCase` and `TestResult`, i.e. create communication channel between them.
- (?) Should destroy `TestCase` after its run to release resources. how?
- Shall handle all exception before, during and after test run. 
  On the other hand `test_frw` may raise exceptions related to its function (implementation errors/ constraints).
  Therefore, return code shall always be 0 if called as module.
  In case there's some error with `test_frw` itself, return code may be other than 0.

#### TestSuite

- Shall group `TestCase`-s.
- (?) Should provide possibility to sort, prioritize test cases.
- (?) Shall provide mechanism for getting test cases one by one (like pop from stack).

#### TestLoader

- Shall locate test cases
- (?)Group test cases to `TestSuite` and pass to `TestRunner`.

#### Fixture

(?) What is fixture? 

Fixture properties: 
- Has its own scope of execution, defined by test sequence.
  E.g. its setup can be called before test1, teardown called after test1, test2 or test3 depending on config.
- Only available for test suites, i.e. more than one test to run.
- Shall be accessible within test namespace.
- (?) Acts as a setup and teardown for any test case.

## ToDo
- Should be possibility to run tests in parallel.
- (?) How the output of the test case should be handled?
    - Printed to the stdout / not printed
    - Stored / not stored
- (?) Implement api for checker: on_check, on_passed, on_failed...
- (?) Implement "between" comparison.
- (?) Modify traceback-s to show only line where comparison is fired.
- Implement text test writer.
- Improve exception info logging.
- delegate `TestCase` instance creation to `TestRunner` like it is defined above: 
  > `TestRunner` Shall create instance of the `TestCase`
