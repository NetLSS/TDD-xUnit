import TestCase
import WasRun


class TestCaseTest(TestCase.TestCase):
    def testRunning(self):
        test = WasRun.WasRun("testMethod")
        assert (not test.wasRun)
        test.run()
        assert (test.wasRun)

    def testSetUp(self):
        test = WasRun.WasRun("testMethod")
        test.run()
        assert (test.wasSetUp)


if __name__ == '__main__':
    TestCaseTest("testRunning").testRunning()
    TestCaseTest("TestSetUp").run()
