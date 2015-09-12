from tabletteChecker import TabletteChecker
from tometteChecker import TometteChecker

def testMockTablette():
    tabChecker = TabletteChecker()
    tabChecker.setMockMode()
    return tabChecker.test()

def testMockTomette():
    tomChecker = TometteChecker()
    tomChecker.setMockMode()
    return tomChecker.test()

def test():
    (statusCode, msg) = testMockTablette()
    if statusCode != 1:
        return (statusCode, msg)

    (statusCode, msg) = testMockTomette()
    if statusCode != 1:
        return (statusCode, msg)
    
    return (1, "")
