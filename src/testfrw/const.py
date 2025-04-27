"""Constants."""

from enum import Enum, IntEnum, auto

class CheckResult(Enum):
    """Result of the check of assert performed by the test case."""
    PASS = 0
    FAIL = 1
    ERROR = 2

class TestVerdict(IntEnum):
    """Single test verdict."""

    # Values do matter.
    # They define the priority of the verdict set.
    # Higher the value, higher the priority.
    # Lower priority cannot be overridden by high priority.
    # E.g. if `PASS = 1` is set and `FAIL = 3` comes, verdict is changed.
    # Otherwise, if `FAIL = 3` is set and `PASS = 1` comes, verdict stays unchanged.
    # See `TestResult.update_verdict` method.

    # Test was successfully run and finished.
    # No assertions were performed. E.g. user didn't use any assert nor check method.
    EMPTY = 0

    # Test was skipped, not performed.
    SKIP = 1

    # Test was successfully run and finished. All checks returned positive result.
    PASS = 2

    # Test was successfully run and finished. One or more checks were failed; or one assert was failed.
    FAIL = 3

    # Some exception was thrown before/ during/ after test `run` method was executed,
    # except the check/ assert exceptions.
    ERROR = 4

class FixtureScope(Enum):
    """Fixture scope. Defines when it shall be run."""

    # At the end of the run not finished fixtures are cleaned: its cleanup() func. is called.

    # Fixture setup is called before any test that uses the fixture.
    # Fixture cleanup is called after test run.
    TEST = auto()

    # Executed only intentionally.
    # Fixture shall be passed as TestCase to the TestRunner.run() func.
    # Fist mention calls its setup. Second mention calls its teardown.
    # Example:
    # TestRunner.run([
    #   Fixture1, # Fixture1.setup is called
    #   TestCase1,
    #   Fixture1, # Fixture1.cleanup is called
    #   TestCase2,
    #   Fixture2, # Fixture2.setup is called
    #   TestCase3,
    #   # Fixture2.cleanup is called automatically at the end of the run
    # ])
    USER = auto()

    # Fixture is executed first when related test case starts.
    # Its cleanup is executed at the end of the run.
    ONCE = auto()

    # Fixture is executed before test run and cleans after test run.
    # Like ONCE but does not depend on the test case.
    AUTO = auto()
