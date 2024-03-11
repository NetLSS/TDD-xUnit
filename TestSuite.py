from TestResult import TestResult

class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test_case):
        self.tests.append(test_case)

    def run(self, result):
        for test in self.tests:
            test.run(result)