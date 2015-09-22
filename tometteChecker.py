from serialChecker import SerialChecker

class TometteChecker(SerialChecker):
    def test(self):
        print "Launch tomette test"
        (statusCode, msg) = self.requestTablette()
        
        if statusCode != 1:
            return (statusCode, msg)
       
        tomettes = self.getTomettesList()
        for i in range(1, len(tomettes)):
            prev = int(tomettes[i-1], 16)
            next = int(tomettes[i], 16)
            if (prev != 0) and (next != 0) and (prev != next):
               return (-1, "Diff:" + ''.join(tomettes))

        return (1, "Tomettes are identical !")

if __name__ == '__main__':
     checker = TometteChecker()
     checker.test()
