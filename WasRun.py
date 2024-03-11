import TestCase


class WasRun(TestCase.TestCase):
    def __init__(self, name):
        self.wasSetUp = None
        self.log = None
        self.wasRun = None
        super().__init__(name)

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception