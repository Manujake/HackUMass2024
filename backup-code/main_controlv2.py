# main_control.py

import serial
import time
import rover_control  # Import the motor control module

# Initialize serial connection to Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # Allow time for the connection to initialize

# Define the obstacle detection threshold (e.g., 20 cm)
OBSTACLE_DISTANCE_THRESHOLD = 40

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
    moving_forward = True  # Track if the rover is currently moving forward

    while True:
        if ser.in_waiting > 0:
            # Read the line of data from Arduino
            line = ser.readline().decode('utf-8').strip()
            print("Raw data:", line)

            # Parse the sensor data
            distances = parse_data(line)

            # Check if the front sensor reading (S1) is present
            if "S1" in distances and "S2" in distances and "S3" in distances:
                front_distance = distances["S1"]  # Front sensor
                left_distance = distances["S2"]   # Left sensor
                right_distance = distances["S3"]  # Right sensor

                print("Front Distance:", front_distance, "cm")
                print("Left Distance:", left_distance, "cm")
                print("Right Distance:", right_distance, "cm")

                # Check for obstacle in front
                if front_distance < OBSTACLE_DISTANCE_THRESHOLD:
                    # Obstacle detected in front, stop if currently moving forward
                    if moving_forward:
                        print("Obstacle detected in front! Stopping.")
                        rover_control.stop()
                        moving_forward = False

                    # Try turning right first if right side is clear
                    if right_distance >= OBSTACLE_DISTANCE_THRESHOLD:
                        print("Right side is clear. Turning right.")
                        rover_control.turn_right()
                        time.sleep(0.4)  # Turn right for 0.4 seconds
                        rover_control.stop()  # Stop after turning

                        # Check front distance again after the turn
                        if "S1" in distances and distances["S1"] >= OBSTACLE_DISTANCE_THRESHOLD:
                            print("Path is clear after turning right. Moving forward.")
                            rover_control.move_forward()
                            moving_forward = True
                            continue  # Skip to next loop iteration

                    # If right side is blocked, check left side
                    elif left_distance >= OBSTACLE_DISTANCE_THRESHOLD:
                        print("Left side is clear. Turning left.")
                        rover_control.turn_left()
                        time.sleep(0.4)  # Turn left for 0.4 seconds
                        rover_control.stop()  # Stop after turning

                        # Check front distance again after the turn
                        if "S1" in distances and distances["S1"] >= OBSTACLE_DISTANCE_THRESHOLD:
                            print("Path is clear after turning left. Moving forward.")
                            rover_control.move_forward()
                            moving_forward = True
                            continue  # Skip to next loop iteration

                else:
                    # No obstacle in front, resume moving forward if currently stopped
                    if not moving_forward:
                        print("Path is clear. Moving forward.")
                        rover_control.move_forward()
                        moving_forward = True

            print()  # Blank line for readability

        time.sleep(0.2)  # Small delay to reduce CPU usage

except KeyboardInterrupt:
    print("Program stopped by user.")
    rover_control.stop()  # Stop the rover when the program is interrupted

finally:
    ser.close()
    rover_control.cleanup()  # Clean up GPIO settings
