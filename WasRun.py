import TestCase


class WasRun(TestCase.TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)

    def testMethod(self):
        self.wasRun = 1

    def run(self):
        method = getattr(self, self.name)
        method()
