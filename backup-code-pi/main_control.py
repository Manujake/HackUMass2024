# main_control.py

import serial
import time
import rover_control  # Import the motor control module

# Initialize serial connection to Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # Allow time for the connection to initialize

def parse_data(data):
    distances = {}
    try:
        # Split data by semicolons and parse each sensor reading
        for sensor_data in data.split(";"):
            if sensor_data:
                sensor_id, distance = sensor_data.split(":")
                distances[sensor_id] = int(distance)
    except ValueError:
        print("Error parsing data")
    return distances

try:
    while True:
        if ser.in_waiting > 0:
            # Read the line of data from Arduino
            line = ser.readline().decode('utf-8').strip()
            print("Raw data:", line)

            # Parse the sensor data
            distances = parse_data(line)

            # Check if all sensor readings are present
            if "S1" in distances and "S2" in distances and "S3" in distances and "S4" in distances:
                # Assign sensors to directions
                front_distance = distances["S1"]  # Front sensor
                left_distance = distances["S2"]   # Left sensor
                right_distance = distances["S3"]  # Right sensor
                back_distance = distances["S4"]   # Back sensor

                print("Front Distance:", front_distance, "cm")
                print("Left Distance:", left_distance, "cm")
                print("Right Distance:", right_distance, "cm")
                print("Back Distance:", back_distance, "cm")

                # Motor control logic based on sensor distances
                if front_distance < 20:
                    print("Obstacle detected in front! Stopping or moving backward.")
                    rover_control.stop()  # Stop motors

                    # Optionally, move backward if the back is clear
                    if back_distance > 20:
                        print("Moving backward to avoid front obstacle.")
                        rover_control.move_backward()

                elif back_distance < 20:
                    print("Obstacle detected at the back! Stopping or moving forward.")
                    rover_control.stop()

                    # Optionally, move forward if the front is clear
                    if front_distance > 20:
                        print("Moving forward to avoid back obstacle.")
                        rover_control.move_forward()

                elif left_distance < 20:
                    print("Obstacle detected on the left! Turning right.")
                    rover_control.turn_right()  # Turn right to avoid left obstacle

                elif right_distance < 20:
                    print("Obstacle detected on the right! Turning left.")
                    rover_control.turn_left()  # Turn left to avoid right obstacle

                else:
                    print("Path is clear. Moving forward.")
                    rover_control.move_forward()  # Move forward if no obstacles are detected

            print()  # Blank line for readability

        time.sleep(0.5)  # Small delay to reduce CPU usage

except KeyboardInterrupt:
    print("Program stopped by user.")
    rover_control.stop()  # Stop the rover when the program is interrupted

finally:
    ser.close()
    rover_control.cleanup()  # Clean up GPIO settings
