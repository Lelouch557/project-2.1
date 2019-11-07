from time import sleep

import serial
import shutter

ser = serial.Serial('COM5', 19200, timeout=1, parity=serial.PARITY_EVEN, rtscts=1)
T = 'TEMP'.encode()
while True:
    sleep(1)
    getVal = ser.readline()
    print(getVal)