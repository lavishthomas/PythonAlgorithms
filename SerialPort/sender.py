import serial
from time import sleep

port = "COM2"
ser = serial.Serial(port, 38400, timeout=0)

while True:
    data = ser.read(9999)
    if len(data) > 0:
        print ('Got: ', data)

    sleep(0.5)
    print ('not blocked')
    x = ser.write(str.encode('0101'))
    sleep (2)


ser.close()


