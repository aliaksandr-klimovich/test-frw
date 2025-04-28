"""This module is for debugging purposes and presents as lightweight example."""

from logger import log

from testfrw.case import TestCase
from testfrw.runner import TestRunner

class DbClient:
    def __init__(self):
        log.info('db client - init')

    def connect(self):
        log.info('db client - connect')

    def disconnect(self):
        log.info('db client - disconnect')

    def __repr__(self):
        return 'DbClient()'

    def __str__(self):
        return 'database client'

class SomeFixture:
    def __init__(self):
        raise RuntimeError('no instance shall be created?')

    ## 3 steps shall be defined:
    #
    ## 1. fixture setup that sets this class properties
    #  or maybe make __init__ as a setup instead?
    @staticmethod
    def fixture_setup():
        SomeFixture.db = DbClient()
        SomeFixture.db.connect()

    ## 2. fixture cleanup/ teardown that cleans resources
    @staticmethod
    def fixture_cleanup():
        SomeFixture.db.disconnect()

    # (?)
    ## 3. some method that assigns the entity to a test class.
    #  `self` is the test case instance.
    def test_setup(self):
        self.db = SomeFixture.db

class TestCase1(TestCase, SomeFixture):
    def run(self):
        # debug

        # fixture setup shall be called by test runner before test call
        SomeFixture.fixture_setup()
        # this method shall be called by test runner too
        self.test_setup()

        log.info(self.db)
        # alternative usage? : (but without IDE code completion)
        log.info(SomeFixture.db)
        self.assert_true(True)

        #
        SomeFixture.fixture_cleanup()

class TestCase2(TestCase):
    def run(self):
        self.check_true(True)

# user defines when fixtures run
TestRunner.run([
    SomeFixture,  # setup
    TestCase1,
    TestCase2,
    SomeFixture,  # cleanup
    TestCase1,  # rerun testcase1
    SomeFixture,  # setup and teardown ?
])
