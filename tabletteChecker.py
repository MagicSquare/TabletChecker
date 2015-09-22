from serialChecker import SerialChecker

class TabletteChecker(SerialChecker):
     # 1k   2k   1k   2k
     # 3k   3.9k 3k   3.9k
     # 5.1k 7.5k 5.1k 7.5k
    _target = ['C0', 'AD', 'C0', 'AD', 
               'A2', '98', 'A2', '98', 
               '8B', '79', '8B', '79']

    def test(self):
        print "Launch tablette test"
        (statusCode, msg) = self.requestTablette()

        if statusCode != 1:
            return (statusCode, msg)

        if self.getTomettesList() != self._target:
            return (-1, "Diff:" + ''.join(self.getTomettesList()))

        return (1, "Tomettes are identical !")

if __name__ == '__main__':
    checker = TabletteChecker()
    checker.test()
