import serial
import time

class SerialChecker:
    _ser = None
    _mockModeOn = False
    __nbTomettes = None
    __nbTomettesByLine = None
    __tomettesList = None
    __checksum = None

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
            result = result + self._ser.read(1)
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

        checkSum = tomettes[int(nbTomettes)*2:]
        if not checkSum or len(checkSum) == 0:
            return (-1, "No checksum found")
        checkSum = int(checkSum, 16)

        if tomettesSum != checkSum :
            return (-1, result)
        else:
            self.__nbTomettes = nbTomettes
            self.__nbTomettesByLine = nbTometteByLine
            self.__tomettesList = tomettesArray
            self.__checkSum = checkSum
            return (1, "")
