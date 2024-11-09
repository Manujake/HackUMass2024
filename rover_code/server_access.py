from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to handle cross-origin requests from AWS S3

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    direction = data.get('direction')
    print(f"Received direction command: {direction}")

    # Process the direction (e.g., control GPIO pins on Raspberry Pi)
    # Example:
    if direction == 'f':
        # Move forward
        print("moving forward")
    elif direction == 'b':
        # Move backward
        print("moving backward")
    elif direction == 'l':
        # Turn left
        print("turning left")
    elif direction == 'r':
        # Turn right
        print("tuning right")
    elif direction == 's':
        # Stop
        print("stopping")

    return {'status': 'success', 'received': direction}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)