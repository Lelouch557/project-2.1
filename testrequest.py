import serial

ser = serial.Serial('COM5', 38400, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
s = ser.read(100)