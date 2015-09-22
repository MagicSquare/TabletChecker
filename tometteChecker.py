from serialChecker import SerialChecker

class TometteChecker(SerialChecker):
    def test(self):
        print "Launch tomette test"
        (statusCode, msg) = self.requestTablette()
        
        if statusCode != 1:
            return (statusCode, msg)
       
        tomettes = self.getTomettesList()
        for i in range(1, len(tomettes)):
            prev = tomettes[i-1]
            next = tomettes[i]
            if (int(prev,16) != 0) and (int(next,16) != 0) and (self.getTometteValue(prev) != self.getTometteValue(next)):
               return (-1, "Diff:" + ''.join(tomettes))

        return (1, "Tomettes are identical !")

if __name__ == '__main__':
     checker = TometteChecker()
     checker.test()
