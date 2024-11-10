from pi_to_arduino import ser, send_command
from flask import Flask, request
from flask_cors import CORS
from threading import Lock
import atexit, time


# Flask Set Up
app = Flask(__name__)
CORS(app)  # Enable CORS to handle cross-origin requests from AWS S3

current_direction = None      # Variable to store the current action
action_lock = Lock()          # Lock to manage access to the current action
stop_event = False            # Global flag to signal stop

@app.route('/move', methods=['POST'])
def handle_action():
    global current_direction, stop_event
    direction = request.json.get('direction')   # get the action performed by the AWS
    possible_directions = ['f', 'b', 'l', 'r', 's']

    if direction not in possible_directions:
        return {"status": "error", "message": "Unknown action"}

    with action_lock:
        # Signal any ongoing action to stop if a new action is requested
        if direction != current_direction:
            stop_event = True
            print(f"Stopping current action: {current_direction}")
            time.sleep(1)  # Short delay to allow the previous action to stop

            # Set the new action and clear the stop flag
            current_direction = direction
            stop_event = False
            print(f"New action set: {current_direction}")

    if direction == 's':  # Special case for stop action
        send_command(current_direction)
        print("Stop action completed.")
        return {"status": "completed", "message": "Stop action completed"}

    # Process the new action in a loop
    while not stop_event:
        send_command(current_direction)
        time.sleep(1)   # Optional delay between commands
        print("Moving...")

    return {"status": "interrupted", "message": "Move action was interrupted"}


# Close the serial connection when the app shuts down
@atexit.register
def close_serial():
    if ser.is_open:
        ser.close()
        print("Serial connection closed.")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)