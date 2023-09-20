"""Custom exceptions."""


class TestFrwException(Exception):
    """Base exception."""


class AssertionFail(TestFrwException):
    """Error that is raised when assertion in test case fails."""


class ComparisonError(TestFrwException):
    """Cannot compare objects.

    Proper methods are not implemented in compared objects or the returned result is not of the bool type.
    """
