"""Constants."""

from enum import Enum, IntEnum


class CheckResult(Enum):
    PASS = 0
    FAIL = 1
    ERROR = 2


class TestVerdict(IntEnum):
    EMPTY = 0  # No assertions were performed. E.g. user forgot to write them.
    SKIP = 1  # Test was skipped, not performed.
    PASS = 2  # Test was successfully run and finished. All checks returned positive result.
    FAIL = 3  # Test was successfully run and finished. One or more checks were failed.
    ERROR = 4  # Test was not inited or was run and threw an exception.
