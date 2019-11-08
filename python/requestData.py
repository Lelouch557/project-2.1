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
        else:
            print("Can't open connection")

    def encode_string(self, string):
        ret = (string + "\r").encode()
        return ret

    def temp(self):
        self.ser.write(self.encode_string("TEMP"))
        return self.ser.readline()

    def light(self):
        self.ser.write(self.encode_string("LIGHT"))
        return self.ser.readline()

    def distance(self):
        self.ser.write(self.encode_string("DISTANCE"))
        return self.ser.readline()

    def down(self):
        self.ser.write(self.encode_string("DOWN"))
        return self.ser.readline()

    def up(self):
        self.ser.write(self.encode_string("UP"))
        return self.ser.readline()

    def close_connection(self):
        self.ser.close()

