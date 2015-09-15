from serialChecker import SerialChecker

class TometteChecker(SerialChecker):
    def test(self):
        (statusCode, msg) = self.requestTablette()
        
        if statusCode != 1:
            return (statusCode, msg)
       
        tomettes = self.getTomettesList()
        for i in range(1, len(tomettes)):
            if tomettes[i-1] != tomettes[i]:
               return (-1, "Diff:" + ''.join(tomettes))

        return (1, "Tomettes are identical !")
