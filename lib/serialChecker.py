import serial

class SerialChecker:
    _ser = None
    _mockModeOn = False

    def setMock(self, mock):
        self._mockModeOn = True
        self._ser = mock

    def requestTablette(self):      
        self._open()
        self._sendL()
        result = self._readTablette()
        self._close()
        return result

    def _open(self):
        if not self._mockModeOn:
            self._ser = serial.Serial('/dev/ttyAMA0',  9600, timeout = 1)
            self._ser.flush()

    def _close(self):
        if not self._mockModeOn:
            self._ser.close()

    def _sendL(self):
        self._ser.write("L")

    def _readTablette(self):
        result = ""
        while self._ser.inWating():
            result = result + self._ser.read(1)
        return result

