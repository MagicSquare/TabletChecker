class MockTablette:
    firstRead = True

    def write(self, data):
        pass

    def read(self, nbBytes):
        self.firstRead = False
        return "12/4/C0ADC0ADA298A2988B798B79756"

    def inWating(self):
        return self.firstRead
