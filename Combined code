import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins for the HC-SR04 sensor
TRIG = 23
ECHO = 24

# Set up the sensor pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Ensure the trigger is low initially
    GPIO.output(TRIG, False)
    time.sleep(0.2)

    # Send a 10µs pulse to trigger the sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for the echo and calculate the pulse duration
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # Calculate distance in centimeters
    distance = pulse_duration * 17150
    return round(distance, 2)

def exclude_large_distances(distances):
    # Calculate the average of the batch
    batch_average = sum(distances) / len(distances)

    # Exclude values greater than 50% above the batch average
    threshold = 1.5 * batch_average
    filtered_distances = [d for d in distances if d <= threshold]

    return filtered_distances

try:
    batch = []
    
    while True:
        # Measure distance and add to the batch
        distance = get_distance()
        print("Measured Distance:", distance, "cm")
        batch.append(distance)

        # Process the batch every 5 readings
        if len(batch) == 5:
            # Exclude values that are more than 50% above the batch average
            filtered_distances = exclude_large_distances(batch)
            print("Filtered Distances:", filtered_distances)

            # Reset the batch for the next set of readings
            batch = []

        time.sleep(1)  # Delay between measurements

except KeyboardInterrupt:
    print("Measurement stopped by User")

finally:
    GPIO.cleanup()
