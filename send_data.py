import serial
import time
ordre = ""

SerialObj = serial.Serial('/dev/ttyACM0') # COMxx  format on Windows
                  # ttyUSBx format on Linux
SerialObj.baudrate = 115200  # set Baud rate to 9600
SerialObj.bytesize = 8   # Number of data bits = 8
SerialObj.parity  ='N'   # No parity
SerialObj.stopbits = 1   # Number of Stop bits = 1
time.sleep(3)

if ordre == "S":
    SerialObj.write(b'S')    #transmit 'S' (8bit) to micro/Arduino
elif ordre == "N":
    SerialObj.write(b'N')    #transmit 'N' (8bit) to micro/Arduino

print(ordre)
SerialObj.close()      # Close the port