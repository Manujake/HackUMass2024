#!/bin/bash
sleep 30

# Navigate to the Desktop
cd ~/Desktop

sleep 1

# Activate the virtual environment
source ./hackathon/bin/activate

sleep 1

# Start the Flask server (assuming the server file is `server_access.py`)
nohup python server_access.py &

sleep 5

# Run Ngrok to forward port 5000
nohup /usr/local/bin/ngrok http --domain=vital-dear-rattler.ngrok-free.app 5000 > ~/ngrok.log 2>&1 &