#!/usr/bin/python3
"""7-states_list.py module"""
from flask import Flask, render_template


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


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp_route(n):
    """
    displays HTML page only if
    n is integer
    """
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_even(n):
    """
    displays HTML page only if
    n is an integer
    """
    mod = n % 2
    if mod > 0:
        num = "{} is odd".format(n)
    else:
        num = "{} is even".format(n)
    return render_template("6-number_odd_or_even.html", num=num)


@app.teardown_appcontext


@app.route("/states_list", strict_slashes=False)
def state_route():
    """method displays states_list HTML page"""
    return render_template("7-states_list.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
