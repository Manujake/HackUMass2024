import serial
import time
import serial.tools.list_ports

def find_serial_port():
    # Look for all connected USB or ACM devices
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "USB" in port.device or "ACM" in port.device:
            # Return the port name if a USB or ACM device is found
            return port.device
    return None  # Return None if no device is found

# print(find_serial_port())

ser = serial.Serial(find_serial_port(), 9600, timeout=1)

def send_command(command):
    ser.write(command.encode('utf-8'))
    print(f"Sent command to Arduino: {command}")
    time.sleep(5)

# Example usage
# commands = ['f', 'b', 'r', 'l', 's']
# for command in commands:
#     send_command(command)
#     time.sleep(5)

# for i in range(10):
#     send_command('f')
#     time.sleep(5)

# Close after sending all commands
# ser.close()