import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def send_command(command):
    ser.write(command.encode('utf-8'))
    print(f"Sent command: {command}")
    # time.sleep(5)

# Example usage
# commands = ['f', 'b', 'r', 'l', 's']
# for command in commands:
#     send_command(command)
#     time.sleep(10)

# for i in range(10):
#     send_command('f')
#     time.sleep(5)
send_command('f')
time.sleep(5)
send_command('l')
time.sleep(5)
send_command('r')
time.sleep(5)
send_command('s')


# Close after sending all commands
ser.close()