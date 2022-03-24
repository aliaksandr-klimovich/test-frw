class TestCase:
    def run(self):
        pass

    def assert_equals(self, measured, expected):
        result = measured == expected
        return result
