import time

class TabletteChecker:
    mockMode = False    

    def setMockMode(self):
        self.mockMode = True

    def test(self):
        print self.mockMode
        time.sleep(5)
        return (1, "Tablette")
