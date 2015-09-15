from tabletteChecker import TabletteChecker
from mockTablette import MockTablette
from tometteChecker import TometteChecker
from mockTomette import MockTomette

def testMockTablette():
    tabChecker = TabletteChecker()
    tabChecker.setMock(MockTablette())
    return tabChecker.test()

def testMockTomette():
    tomChecker = TometteChecker()
    tomChecker.setMock(MockTomette())
    return tomChecker.test()

def test():
    (statusCode, msg) = testMockTablette()
    if statusCode != 1:
        return (statusCode, msg)

    (statusCode, msg) = testMockTomette()
    if statusCode != 1:
        return (statusCode, msg)
    
    return (1, "")
