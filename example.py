"""This module is for debugging purposes and presents as lightweight example."""

from case import TestCase
from fixture import Fixture
from result import TestResult
from runner import TestRunner

class Fixture1(Fixture):
    def setup(self):
        print('db - open connection')
        self.db = 'db'

    def cleanup(self):
        print('db - close connection')
        self.db = None

class Fixture2(Fixture):
    def setup(self):
        print('ssh - open connection')
        self.ssh = 'ssh'

    def cleanup(self):
        print('ssh - close connection')
        self.ssh = None

class TestCase1( TestCase, Fixture1, Fixture2 ):
    def setup(self):
        Fixture1.setup(self)
        Fixture2.setup(self)

    def run(self):
        self.result=TestResult()
        print(self.db)
        print(self.ssh)
        self.assert_true(True)


TestRunner.run1(TestCase1)