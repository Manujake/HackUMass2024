from flask import Flask, request
from flask_cors import CORS
# from pi_to_arduino import ser, send_command
import time
import atexit
import serial



app = Flask(__name__)
CORS(app)  # Enable CORS to handle cross-origin requests from AWS S3
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)


@app.route('/move', methods=['POST'])
def move():
    data = request.json
    direction = data.get('direction')
    if direction:
        ser.write(direction.encode('utf-8'))
        time.sleep(5)
        print(f"Sent command to Arduino: {direction}")
    return {'status': 'success', 'received_direction': direction}, 200


# Close the serial connection when the app shuts down
@atexit.register
def close_serial():
    if ser.is_open:
        ser.close()
        print("Serial connection closed.")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)