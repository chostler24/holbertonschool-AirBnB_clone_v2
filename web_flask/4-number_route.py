#!/usr/bin/python3
"""4-number_route.py module"""
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
def c_route(text):
    """
    method returns C, value of text and
    changes underscore to blank space
    """
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """
    method returns Python, value of text
    and changes underscore to blank space
    """
    text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """
    method returns n is a number
    only if n is an integer
    """
    return ("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
