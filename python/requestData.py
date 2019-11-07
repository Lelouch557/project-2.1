from time import sleep
import serial

class RequestData:
    def __init__(self, comp):
        self.ser = serial.Serial()
        self.ser.baudrate=19200
        self.ser.port = comp
        self.ser.open()
        if(self.ser.isOpen()):
            self.ser.readline()
            return "ok"
        else:
            return "Can't open connection"

    def encode_string(self, string):
        ret = (string + "\n\r").encode()
        return ret

    def temp(self):
        self.ser.write(self.encode_string("TEMP"))

    def light(self):
        self.ser.write(self.encode_string("LIGHT"))

    def distance(self):
        self.ser.write(self.encode_string("DISTANCE"))

    def down(self):
        self.ser.write(self.encode_string("DOWN"))

    def up(self):
        self.ser.write(self.encode_string("UP"))

    def close_connection(self):
        self.ser.close()