#!/usr/bin/python3
import time
import serial

# Jetson nano 수신부
jet_rx = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

# Wait a second to let the port initialize
time.sleep(1)

while True:
    try:
        if jet_rx.readable():
            msg = jet_rx.readline().decode()
            print(msg[:len(msg)-1] + '   {}bytes'.format(len(msg)))

    except Exception as e:
        print(e)

