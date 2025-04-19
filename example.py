"""This module is for debugging purposes and presents as lightweight example."""

import hooks
from case import TestCase
from const import TestVerdict
from runner import TestRunner

class Fixture:
    scope = 'test'

    instance = None


    # prohibit to create instance of the same fixture multiple times when TestCase instance is created
    #
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(*args, **kwargs)
        return cls.instance

    def setup(self):
        pass

    def cleanup(self):
        pass

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

class TestCase1( Fixture1, Fixture2, TestCase ):
    def run(self):
        print(self.db)
        print(self.ssh)


TestRunner.run1(TestCase1)