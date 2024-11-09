import rover_control as rover
from flask import Flask, request

app = Flask(__name__)


# Endpoint to receive commands
@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    direction = data.get('direction')
    if direction == 'forward':
        rover.move_forward
    elif direction == 'backward':
        rover.move_backward()
    elif direction == 'left':
        rover.turn_left()
    elif direction == 'right':
        rover.turn_right()
    return 'Command executed', 200