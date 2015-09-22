import serial
import time

class SerialChecker:
    _ser = None
    _mockModeOn = False
    __nbTomettes = None
    __nbTomettesByLine = None
    __tomettesList = None
    __checksum = None
    __tomettesTolerance = [
        ['79', '75', '76', '77', '78', '7A', '7B', '7C', '7D', '7E'],
        ['82', '7F', '80', '81', '83', '84', '85', '86', '87', '88'],
        ['8B', '86', '87', '88', '89', '8A', '8C', '8D', '8E', '8F', '90'],
        ['98', '93', '94', '95', '96', '97', '99', '9A', '9B', '9C', '9D'],
        ['A2', '9E', '9F', 'A0', 'A1', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'],
        ['AD', 'A9', 'A0', 'AB', 'AC', 'AE', 'AF', 'B0', 'B1', 'B2', 'B3'],
        ['C0', 'BB', 'BC', 'BD', 'BE', 'BF', 'C1', 'C2', 'C3', 'C4', 'C5']
    ]

    def setMock(self, mock):
        self._mockModeOn = True
        self._ser = mock

    def requestTablette(self):      
        self._open()
        self._sendL()
        result = self._readTablette()
        print result
        self._close()
        return self._extractData(result)

    def getTomettesList(self):
        return self.__tomettesList

    def _open(self):
        if not self._mockModeOn:
            print "Open serial communication..."
            self._ser = serial.Serial('/dev/ttyAMA0',  9600, timeout = 1)
            self._ser.flush()
            print "OK"

    def _close(self):
        if not self._mockModeOn:
            self._ser.close()

    def _sendL(self):
        print "Send L"
        nbBytesWritten = self._ser.write("L")
        print "Write " + str(nbBytesWritten) + " bytes"

    def _readTablette(self):
        if self._mockModeOn:
            return self._ser.read(1)
        result = ""
        lastResult = ""
        loop = True
        while result == "" or result != lastResult:
            print "Read 1 byte"
            print lastResult
            print result
            lastResult = result
            time.sleep(1)
            result = result + self._ser.read(40)
        print "Read : " + result
        
        # Remove L character
        return result[1:]

    def _extractData(self, result):
        print "Extracting " + result
        try:
             (nbTomettes, nbTometteByLine, tomettes) = result.split("/")
        except:
            return (-1, "Syntax error:" + result)

        if (len(tomettes) / 2) < int(nbTomettes):
            return (-1, "Not enough data:" + nbTomettes + "/" + str(len(tomettes)))

        tomettesSum = 0
        tomettesArray = []
        for i in range(int(nbTomettes)):
            tometteValue = tomettes[i*2] + tomettes[i*2+1]
            tomettesSum += int(tometteValue, 16)
            tomettesArray.append(tometteValue)
        tomettesSum = hex(tomettesSum)[-2:]

        checkSum = tomettes[int(nbTomettes)*2:]
        if not checkSum or len(checkSum) == 0:
            return (-1, "No checksum found")

        if tomettesSum.strip().upper() != checkSum.strip().upper() :
            return (-1, "Check:" + result)
        else:
            self.__nbTomettes = nbTomettes
            self.__nbTomettesByLine = nbTometteByLine
            self.__tomettesList = tomettesArray
            self.__checkSum = checkSum
            return (1, "")

    def getTometteValue(self, tomette):
        for tolerance in self.__tomettesTolerance:
            if tomette in tolerance:
                return tolerance[0]
        return tomette
