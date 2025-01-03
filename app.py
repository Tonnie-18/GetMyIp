import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # Get the client's IP address
    client_ip = request.remote_addr
    
    # Fetch the server's public IP address using ipify
    server_ip = requests.get('https://api.ipify.org').text

    # Display both client and server IP addresses
    return f"Your IP address is: {client_ip}<br>Server's public IP address is: {server_ip}"

if __name__ == '__main__':
    app.run(debug=True)
