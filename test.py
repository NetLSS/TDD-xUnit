import WasRun

if __name__ == '__main__':
    test = WasRun.WasRun("testMethod")
    print(test.wasRun)
    test.testMethod()
    print(test.wasRun)