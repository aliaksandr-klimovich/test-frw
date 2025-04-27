"""This module is for debugging purposes and presents as lightweight example."""

from testfrw.case import TestCase
from testfrw.fixture import Fixture
from testfrw.result import TestResult
from testfrw.runner import TestRunner

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

# TypeError: Cannot create a consistent method resolution order (MRO) for bases Fixture, Fixture1
# class Fixture3(Fixture, Fixture1):
#     pass

class TestCase1( TestCase, Fixture1, Fixture2 ):
    def run(self):
        print(self.db)
        print(self.ssh)
        self.assert_true(True)

res = TestRunner.run([TestCase1])
print(res)
