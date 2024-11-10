from pi_to_arduino import ser, send_command
from flask import Flask, request
from flask_cors import CORS
import atexit


# Fask Set Up
app = Flask(__name__)
CORS(app)  # Enable CORS to handle cross-origin requests from AWS S3


# Handle POST methods (HTML) from the AWS S3 User Interface
@app.route('/move', methods=['POST'])
def move():
    data = request.json
    direction = data.get('direction')
    if direction:
        send_command(direction)
        # ser.write(direction.encode('utf-8'))
        # print(f"Sent command to Arduino: {direction}")
        # time.sleep(5)
        
    return {'status': 'success', 'received_direction': direction}, 200


# Close the serial connection when the app shuts down
@atexit.register
def close_serial():
    if ser.is_open:
        ser.close()
        print("Serial connection closed.")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)