import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # Set Trigger to HIGH
    GPIO.output(TRIG, True)
    # Set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Measure the echo response time
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    # Calculate distance (Speed of sound: 34300 cm/s)
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
