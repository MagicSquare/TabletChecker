class MockTomette:
    firstRead = True

    def write(self, data):
        pass

    def read(self, nbBytes):
        self.firstRead = False
        return "Tomette"

    def inWating(self,):
        return self.firstRead
