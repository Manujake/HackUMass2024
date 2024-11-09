#rover_control.py


import RPi.GPIO as GPIO
import time

# Motor GPIO pin definitions
FL_IN1 = 17  # Front Left motor input pin 1
FL_IN2 = 27  # Front Left motor input pin 2
FR_IN1 = 22  # Front Right motor input pin 1
FR_IN2 = 23  # Front Right motor input pin 2
BL_IN1 = 5   # Back Left motor input pin 1
BL_IN2 = 6   # Back Left motor input pin 2
BR_IN1 = 13  # Back Right motor input pin 1
BR_IN2 = 19  # Back Right motor input pin 2

# Enable pins (for PWM control)
FL_ENABLE = 18  # Front Left enable pin
FR_ENABLE = 24  # Front Right enable pin
BL_ENABLE = 12  # Back Left enable pin
BR_ENABLE = 25  # Back Right enable pin

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup each pin as output
motor_pins = [FL_IN1, FL_IN2, FR_IN1, FR_IN2, BL_IN1, BL_IN2, BR_IN1, BR_IN2]
enable_pins = [FL_ENABLE, FR_ENABLE, BL_ENABLE, BR_ENABLE]

for pin in motor_pins + enable_pins:
    GPIO.setup(pin, GPIO.OUT)

# Setup PWM for enable pins with 1000 Hz frequency
FL_PWM = GPIO.PWM(FL_ENABLE, 1000)
FR_PWM = GPIO.PWM(FR_ENABLE, 1000)
BL_PWM = GPIO.PWM(BL_ENABLE, 1000)
BR_PWM = GPIO.PWM(BR_ENABLE, 1000)

# Start PWM with 0 duty cycle (motors initially off)
FL_PWM.start(0)
FR_PWM.start(0)
BL_PWM.start(0)
BR_PWM.start(0)

# Helper function to control motor direction
def move_motor(in1, in2, direction):
    """Controls motor direction."""
    if direction == 'forward':
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
    elif direction == 'backward':
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
    elif direction == 'stop':
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)

# Function to set motor speed
def set_speed(duty_cycle):
    """Sets the speed of all motors by adjusting PWM duty cycle."""
    FL_PWM.ChangeDutyCycle(duty_cycle)
    FR_PWM.ChangeDutyCycle(duty_cycle)
    BL_PWM.ChangeDutyCycle(duty_cycle)
    BR_PWM.ChangeDutyCycle(duty_cycle)

# Movement functions
def move_forward(speed=80):
    """Moves the rover forward at a specified speed."""
    set_speed(speed)
    move_motor(FL_IN1, FL_IN2, 'forward')
    move_motor(FR_IN1, FR_IN2, 'forward')
    move_motor(BL_IN1, BL_IN2, 'forward')
    move_motor(BR_IN1, BR_IN2, 'forward')
    print("Moving Forward")

def move_backward(speed=80):
    """Moves the rover backward at a specified speed."""
    set_speed(speed)
    move_motor(FL_IN1, FL_IN2, 'backward')
    move_motor(FR_IN1, FR_IN2, 'backward')
    move_motor(BL_IN1, BL_IN2, 'backward')
    move_motor(BR_IN1, BR_IN2, 'backward')
    print("Moving Backward")

def turn_left(speed=60):
    """Performs a left turn using diagonal motors at a specified speed."""
    set_speed(speed)
    move_motor(FR_IN1, FR_IN2, 'forward')  # Front Right moves forward
    move_motor(BL_IN1, BL_IN2, 'backward')  # Back Left moves backward
    move_motor(FL_IN1, FL_IN2, 'stop')      # Front Left stops
    move_motor(BR_IN1, BR_IN2, 'stop')      # Back Right stops
    print("Turning Left with Diagonal Motors")

def turn_right(speed=60):
    """Performs a right turn using diagonal motors at a specified speed."""
    set_speed(speed)
    move_motor(FL_IN1, FL_IN2, 'forward')   # Front Left moves forward
    move_motor(BR_IN1, BR_IN2, 'backward')  # Back Right moves backward
    move_motor(FR_IN1, FR_IN2, 'stop')      # Front Right stops
    move_motor(BL_IN1, BL_IN2, 'stop')      # Back Left stops
    print("Turning Right with Diagonal Motors")

def stop():
    """Stops all motors."""
    for pin in motor_pins:
        GPIO.output(pin, GPIO.LOW)
    set_speed(0)  # Stop PWM to all motors
    print("Stopping")

# Cleanup function to release GPIO resources
def cleanup():
    """Cleans up GPIO settings."""
    stop()
    GPIO.cleanup()
