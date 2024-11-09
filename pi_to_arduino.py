import serial
import time

# Replace '/dev/ttyUSB0' with the actual port connected to the Arduino
# ls /dev/ttyUSB* /dev/ttyACM*
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def send_command(command):
    ser.write(command.encode('utf-8'))
    print(f"Sent command: {command}")   # f, b, l ,r, s
    time.sleep(5)

# Example usage
#while(1):
#	send_command('f')  # Forward
send_command('s')
#send_command('r')
#	send_command('l')

ser.close()
