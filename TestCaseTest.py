import TestCase
import WasRun


class TestCaseTest(TestCase.TestCase):

    def setUp(self):
        self.test = WasRun.WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self):
        self.test.run()
        assert self.test.wasSetUp


if __name__ == '__main__':
    TestCaseTest("testRunning").testRunning()
    TestCaseTest("testSetUp").run()
