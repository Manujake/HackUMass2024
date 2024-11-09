### This is for reference
### The raspberrypi will be fetching data from the aws through flask


from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Forward pin
GPIO.setup(18, GPIO.OUT)  # Backward pin
GPIO.setup(22, GPIO.OUT)  # Left turn pin
GPIO.setup(23, GPIO.OUT)  # Right turn pin

def forward():
    GPIO.output(17, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)

def backward():
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)

def left_turn():
    GPIO.output(22, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(22, GPIO.LOW)

def right_turn():
    GPIO.output(23, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23, GPIO.LOW)

@app.route('/')
def index():
    return '''
    <button onclick="location.href='/forward'">Forward</button>
    <button onclick="location.href='/backward'">Backward</button>
    <button onclick="location.href='/left'">Left</button>
    <button onclick="location.href='/right'">Right</button>
    '''

@app.route('/forward')
def move_forward():
    forward()
    return 'Moving Forward'

@app.route('/backward')
def move_backward():
    backward()
    return 'Moving Backward'

@app.route('/left')
def turn_left():
    left_turn()
    return 'Turning Left'

@app.route('/right')
def turn_right():
    right_turn()
    return 'Turning Right'

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()
