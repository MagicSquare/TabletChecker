from serialChecker import SerialChecker

class TabletteChecker(SerialChecker):
     # 1k   2k   1k   2k
     # 3k   3.9k 3k   3.9k
     # 5.1k 6.2k 5.1k 6.2k
    _target = ['C0', 'AD', 'C0', 'AD', 
               'A2', '98', 'A2', '98', 
               '8B', '82', '8B', '82']

    def test(self):
        print "Launch tablette test"
        (statusCode, msg) = self.requestTablette()

        if statusCode != 1:
            return (statusCode, msg)

        i = 0
        for tomette in self.getTomettesList():
           if self.getTometteValue(tomette)  != self._target[i]:
               return (-1, "Diff:" + ''.join(self.getTomettesList()))
           i += 1
        return (1, "Tablette is OK !")

if __name__ == '__main__':
    checker = TabletteChecker()
    checker.test()
