from time import sleep
import serial

ser = serial.Serial()
ser.baudrate=19200
ser.port="COM3"
ser.open()
print(ser.readline())
while ser.isOpen():
    sleep(0.1)
    print('input?')
    T = input()
    if(T == "close"):
        break
    T = (T + "\n\r").encode()
    ser.write(T)
    print(ser.readline())
    print("4")
ser.close()