from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route("/")
def home():
    # Get the client's IP address
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Get the server's IP address
    server_ip = socket.gethostbyname(socket.gethostname())

    # Pass both IPs to the HTML template
    return render_template("index.html", client_ip=client_ip, server_ip=server_ip)

if __name__ == "__main__":
    app.run(debug=True)
