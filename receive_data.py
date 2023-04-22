import serial
import time

SerialObj = serial.Serial('/dev/ttyACM0') # COMxx  format on Windows
SerialObj.baudrate = 115200
ReceivedString = SerialObj.readline()

SerialObj.close() 