import time
from datetime import datetime

from const import CheckResult
from tb_info import TracebackInfo


class Event:
    """
    Base event. Collected during test run.
    """
    def __init__(self):
        self.timestamp = time.time()

    def get_utc_timestamp(self) -> datetime:
        return datetime.utcfromtimestamp(self.timestamp)

    def get_timestamp(self) -> datetime:
        """Returns timestamp for local tz."""
        return datetime.fromtimestamp(self.timestamp)


class FailEvent(Event):
    """
    Explicit fail of the test case by user.
    """
    def __init__(self, message: str = ''):
        super().__init__()
        self.message = message

    def __repr__(self):
        # no timestamp
        return f'FailEvent(message="{self.message}")'


class ErrorEvent(Event):
    """
    Represents error event that was happened during test case instance creation
    or test case execution.
    """
    def __init__(self, tb_info: TracebackInfo = None):
        super().__init__()
        self.tb_info = tb_info

    def __repr__(self):
        # no timestamp
        if self.tb_info is None:
            tb_info = None
        else:
            tb_info = f'TracebackInfo({self.tb_info})'
        return f'ErrorEvent(tb_info={tb_info})'


class CheckEvent(Event):
    """
    Check event that contains result of check_* or assert_* method execution.
    """
    def __init__(self, result: CheckResult = None, tb_info: TracebackInfo = None, message: str = ''):
        super().__init__()
        self.result = result
        self.message = message
        self.tb_info = tb_info


class Check2Event(CheckEvent):
    """
    Check event that contains result of comparison of 2 objects.
    """
    def __init__(self, *args, actual=None, sign=None, expected=None, strict=None, **kwargs):
        """

        :param args:
        :param actual:
        :param sign:
        :param expected:
        :param strict: whereas check_* or assert_* method was called
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.actual = actual
        self.sign = sign
        self.expected = expected
        self.strict = strict

    def __repr__(self):
        # no timestamp
        if isinstance(self.actual, str):
            actual = f'"{self.actual}"'
        else:
            actual = self.actual
        if isinstance(self.expected, str):
            expected = f'"{self.expected}"'
        else:
            expected = self.expected
        if self.tb_info is None:
            tb_info = None
        else:
            tb_info = f'TracebackInfo({self.tb_info})'
        return (
            f'Check2Event('
            f'message="{self.message}"'
            f', actual={actual}'
            f', sign="{self.sign}"'
            f', expected={expected}'
            f', result=CheckResult.{self.result.name}'
            f', strict={self.strict}'
            f', tb_info={tb_info}'
            f')'
        )
