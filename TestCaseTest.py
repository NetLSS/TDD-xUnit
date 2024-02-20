import TestCase
import WasRun

class TestCaseTest(TestCase.TestCase):
    def testRunning(self):
        test = WasRun.WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

if __name__ == '__main__':
    TestCaseTest("testRunning").testRunning()