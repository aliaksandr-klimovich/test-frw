from enum import IntEnum


class TestVerdict(IntEnum):
    EMPTY = 0  # No assertions were performed. E.g. user forgot to write them.
    SKIPPED = 1  # Test was skipped, not performed.
    PASSED = 2  # Test was successfully run and finished. All assertions returned positive result.
    FAILED = 3  # Test was successfully run and finished. One or more assertions were failed.
    ERROR = 4  # Test was run and threw an exception or error.


class TestResult:
    """
    Test results collector.
    Any test result is collected.
    """

    def __init__(self):
        self.test_verdict = TestVerdict.EMPTY

    def update_test_verdict(self, test_verdict: TestVerdict):
        """
        Test verdict is updated any time the assertion is made.
        Most "critical" verdict is selected and stored.
        """
        if test_verdict > self.test_verdict:
            self.test_verdict = test_verdict
