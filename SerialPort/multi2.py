import serial
from time import sleep

port = "COM2"
ser = serial.Serial(port, 38400, timeout=0)

while True:
    data = ser.read(9999)
    if len(data) > 0:
        print ('Got from 1', data)

    sleep(0.5)
    print ('not blocked')

    x = ser.write(str.encode('1111'))
    sleep (2)


ser.close()


