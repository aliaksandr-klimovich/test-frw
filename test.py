from case import TestCase
from runner import TestRunner


class MyTestCase(TestCase):
    def run(self):
        result = self.assert_equals(True, True)
        print('assertion result:', result)


if __name__ == '__main__':
    runner = TestRunner()
    runner.add_test_cases(MyTestCase)
    runner.run()
