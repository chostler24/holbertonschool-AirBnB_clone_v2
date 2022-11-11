#!/usr/bin/python3
"""2-c_route.py module"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """method returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """method returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route():
    """
    method returns C and changes underscore
    to blank space
    """
    return "C"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
