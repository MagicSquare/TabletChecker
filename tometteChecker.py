from serialChecker import SerialChecker

class TometteChecker(SerialChecker):
    def test(self):
        result = self.requestTablette()
        return (1, result)
