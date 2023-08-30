from enum import Enum, IntEnum


class CheckResult(Enum):
    PASSED = 0
    FAILED = 1
    ERROR = 2


class TestVerdict(IntEnum):
    EMPTY = 0  # No assertions were performed. E.g. user forgot to write them.
    SKIPPED = 1  # Test was skipped, not performed.
    PASSED = 2  # Test was successfully run and finished. All assertions returned positive result.
    FAILED = 3  # Test was successfully run and finished. One or more assertions were failed.
    ERROR = 4  # Test was not inited or was run and threw an exception or error.
