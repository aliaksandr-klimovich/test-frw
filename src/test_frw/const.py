"""Constants."""

from enum import Enum, IntEnum

class CheckResult(Enum):
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
