from flask import Flask, jsonify, request
from app import app  # Import the Flask app from app.py
from Database import init_db  # Import database initialization function


# Initialize the database
init_db()

# Define additional routes
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()  # Get JSON payload from the request
    return jsonify({"received_data": data}), 201

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
