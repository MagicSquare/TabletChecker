import time

class TometteChecker:
    mockMode = False

    def setMockMode(self):
        self.mockMode = True

    def test(self):
        time.sleep(5)
        return (1, "Tomette")
