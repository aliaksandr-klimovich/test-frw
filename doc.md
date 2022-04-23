# Documentation

## Requirements

- Test shall be written and located in TestCase class.
- (constraint) Each test case shall contain only one test to run, i.e. only one meaningful test entity.
- TestCase shall contain a method that starts the test.
- Test shall start outside TestCase class by external tool.
- A tool to run TestCase shall be implemented, i.e. TestRunner class.
- TestRunner shall run test(s) in an isolated environment, i.e. thread or process.
- API for TestCase and TestRunner should be implemented to have possibility to extend these classes. I.e. hooks.
- TestResult class shall be implemented. It shall contain information about test case run results.
- ~~TestRunner should return TestResult after TestCase execution.~~
- TestLoader should be implemented to locate test cases and pass them to TestRunner. Or just return a TestSuite.
- TestSuite should be implemented to group tests.
- After test run TestCase should be destroyed and resources should be released.
- TestCase shall contain TestResult as a property.
- Should be possibility to parametrize test case.
- Should be possibility to run tests in parallel.
- TestCase shall contain methods to assert ~~and check~~ entities.
    ~~Assert should cause test fail immediately.~~
    Assert method shall:
    - store failed result,
    - continue test execution if it is possible,
    - at the end of the test "fail" it.
- TestReporter?

## Implementation

- TestCase is a class that contains `run` method.
- TestCase contains TestResult as a property (composition),
    a container for any data that can be retrieved during test run.
- TestRunner executes method `run` of a TestCase in separate process.
- TestCase is extended with Asserter mixin class to be able to use `assert_*` methods inside.
- Asserter class contains `assert_*` methods that return assertion result.
- TestResult contains TestVerdict.

## todo

- Implement communication channel between TestRunner and TestCase.
- ~~Implement communication channel between TestRunner and TestReporter.~~
- TestVerdict shall be updated after any assertion is made.
- Asserter shall store all its input and output in TestResult.