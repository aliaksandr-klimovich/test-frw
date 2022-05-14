"""This module provides Frw related exceptions."""


class TestFrwException(Exception):
    pass


class AssertionFail(TestFrwException):
    """Base exception that is raised when assertion in test case fails."""
    def __init__(self, *args, **kwargs):
        pass
