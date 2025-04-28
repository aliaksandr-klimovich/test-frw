"""Test run events."""

import logging
import time
from datetime import datetime, timezone

from .const import CheckResult
from .exc_info import ExceptionInfo

log = logging.getLogger(__name__)

class Event:
    """Base event.

    These events are collected during test run.
    """
    def __init__(self):
        self.timestamp = time.time()

    def get_utc_timestamp(self) -> datetime:
        return datetime.fromtimestamp(self.timestamp, timezone.utc)

    def get_timestamp(self) -> datetime:
        return datetime.fromtimestamp(self.timestamp)

class FailEvent(Event):
    """Explicit fail of the test case by user."""
    def __init__(self, message: str = ''):
        super().__init__()
        self.message = message

    def __repr__(self):
        return f'FailEvent(message="{self.message}")'

class ErrorEvent(Event):
    """Represents error event that was happened during test case instance creation or test case execution."""
    def __init__(self, exc_info: ExceptionInfo = None):
        super().__init__()
        self.exc_info = exc_info

    def __repr__(self):
        if self.exc_info is None:
            exc_info = None
        else:
            exc_info = f'ExceptionInfo({self.exc_info})'
        return f'ErrorEvent(exc_info={exc_info})'

class CheckEvent(Event):
    """Check event that contains result of check_* or assert_* method execution."""
    def __init__(self, result: CheckResult = None, exc_info: ExceptionInfo = None, message: str = ''):
        super().__init__()
        self.result = result
        self.message = message
        self.exc_info = exc_info

class Check2Event(CheckEvent):
    """Check event that contains result of comparison of 2 objects."""
    def __init__(self, *args, actual=None, sign=None, expected=None, strict=None, **kwargs):
        """Class initialization.

        Args:
            args:
            actual:
            sign:
            expected:
            strict: whereas check_* or assert_* method was called
            kwargs:
        """
        super().__init__(*args, **kwargs)
        self.actual = actual
        self.sign = sign
        self.expected = expected
        self.strict = strict

    def __repr__(self):
        if isinstance(self.actual, str):
            actual = f'"{self.actual}"'
        else:
            actual = self.actual
        if isinstance(self.expected, str):
            expected = f'"{self.expected}"'
        else:
            expected = self.expected
        if self.exc_info is None:
            exc_info = None
        else:
            exc_info = f'ExceptionInfo({self.exc_info})'
        return (
            f'Check2Event('
            f'message="{self.message}"'
            f', actual={actual}'
            f', sign="{self.sign}"'
            f', expected={expected}'
            f', result=CheckResult.{self.result.name}'
            f', strict={self.strict}'
            f', exc_info={exc_info}'
            f')'
        )
