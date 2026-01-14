#!/usr/bin/python3
"""Module for developing a simple API using Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Handle root endpoint."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Return API status."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Return user object by username.
    
    Args:
        username (str): The username to look up.
        
    Returns:
        JSON response with user data or error message.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user to the API.
    
    Expected JSON body:
        {
            "username": "string",
            "name": "string",
            "age": int,
            "city": "string"
        }
        
    Returns:
        JSON response with confirmation or error message.
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400
    
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    users[username] = data
    
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == '__main__':
    app.run()
