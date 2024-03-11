import TestCase
import WasRun


class TestCaseTest(TestCase.TestCase):

    def setUp(self):
        self.test = WasRun.WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun.WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)


if __name__ == '__main__':
    TestCaseTest("testTemplateMethod").run()
