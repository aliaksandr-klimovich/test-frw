"""
This module provides Frw related exceptions.
"""


class TestFrwException(Exception):
    pass


# class TestCaseInitError(TestFrwException):
#     """
#     Raised when test case initialization fails.
#     """


class AssertionFail(TestFrwException):
    """
    Base exception that is raised when assertion in test case fails.
    """


class ComparisonError(TestFrwException):
    """
    Cannot compare objects.
    Proper methods are not implemented in compared objects
     or the returned result is not of the bool type.
    """
    pass
