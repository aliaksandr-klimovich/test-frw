"""
This module is for debugging and presented as lightweight example.
todo: Move this module to `test` folder.
"""

from case import TestCase
from runner import TestRunner


class MyTestCase(TestCase):
    def run(self):
        result = self.assert_eq(False, True)
        print('assertion result 1:', result)

        result = self.assert_eq(True, True)
        print('assertion result 2:', result)


if __name__ == '__main__':
    TestRunner.run(MyTestCase)
