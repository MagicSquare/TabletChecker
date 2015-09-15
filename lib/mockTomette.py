class MockTomette:
    firstRead = True

    def write(self, data):
        pass

    def read(self, nbBytes):
        self.firstRead = False
        return "12/4/C0C0C0C0C0C0C0C0C0C0C0C0900"

    def inWating(self):
        return self.firstRead
