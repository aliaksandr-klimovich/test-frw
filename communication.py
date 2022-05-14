"""
This module provides communication classes (interface) to bind
TestCase and TestResult from TestRunner.
"""


class TestCommunicationChannel:

    def send(self, *args, **kwargs):
        pass

    def recv(self, *args, **kwargs):
        pass
