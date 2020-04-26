import serial
from time import sleep

port = "COM2"

ser = serial.Serial(port, 38400, timeout=0)

print(ser)
while True:
    data = ser.read(9999)
    if len(data) > 0:
        print ('Got from 2 ', data)

    sleep(0.5)
    print ('not blocked')

    x = ser.write(str.encode('2222'))
    sleep (2)


ser.close()


