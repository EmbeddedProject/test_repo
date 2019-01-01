#!/usr/bin/python3

import subprocess
import serial
import time

def cpuload():
    # bashCommand = "mpstat -P ALL | head -4 | awk '{print $3}' | tail -1"
    bashCommand = "top -b -n2 | grep \"Cpu(s)\"|tail -n 1 | awk '{print $2 + $4}'"
    out = subprocess.check_output(['bash','-c', bashCommand])
    #type(out)
    res = out.strip()
    res = res.decode()
    res = float(res.replace(',','.'))
    res = round(res)
    return int(res);

# Main
ser = serial.Serial('/dev/ttyACM0')
ser.baudrate = 115200
# send enter and CTRL+D to reboot the board
ser.write(b'\r')
ser.write(b'\04')

while True:
    load = cpuload()
    print(load)
    load = b'%d\r' % (load+1)
    ser.write(load)
    time.sleep(1)
    



