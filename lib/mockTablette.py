class MockTablette:
    firstRead = True

    def write(self, data):
        pass

    def read(self, nbBytes):
        self.firstRead = False
        return "Tablette"

    def inWating(self):
        return self.firstRead
