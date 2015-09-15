from serialChecker import SerialChecker

class TabletteChecker(SerialChecker):
    def test(self):
        result = self.requestTablette()
        return (1, result)
