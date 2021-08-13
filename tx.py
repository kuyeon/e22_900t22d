#!/usr/bin/python3
import time
import serial
from datetime import datetime

# Jetson nano 송신부
port_num = input("tty: ")

jet_tx = serial.Serial(
    port=f'/dev/tty{port_num}',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

# Wait a second to let the port initialize
time.sleep(1)

num = 0
sleep_rate = 1

while True:
    try:
        msg = 'message'.ljust(20, "-") + f'[{num}]\n'
        msg_len = len(msg)
        jet_tx.write(msg.encode())
        print(f'send_message[{num}], rate: {msg_len}bytes per {sleep_rate}sec')
        num += 1
        now = datetime.now()
        if jet_tx.readable():
            rx_data = jet_tx.readline().decode()
            delay_time = now - datetime.now()
            print(f'{rx_data[:len(rx_data)-1]} -> Delay Time: {(delay_time.microseconds/1000000)/2}sec\n')
        time.sleep(sleep_rate)
    except Exception as e:
        print(e)

